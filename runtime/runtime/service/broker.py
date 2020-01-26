import asyncio
from concurrent.futures import ThreadPoolExecutor
import ctypes
import dataclasses
from numbers import Real
from typing import Mapping

from schema import Optional
import structlog
import zmq
import zmq.asyncio

from runtime.service.base import Service
from runtime.messaging.device import DeviceBuffer, get_device_type
from runtime.messaging.routing import Connection, ConnectionManager
from runtime.util import POSITIVE_INTEGER, POSITIVE_REAL, VALID_NAME
from runtime.util.exception import RuntimeBaseException


LOGGER = structlog.get_logger()


@dataclasses.dataclass
class DatagramClient:
    conn: Connection
    timeout: Real
    pinged: asyncio.Condition = dataclasses.field(default_factory=asyncio.Condition)

    async def keep_alive(self):
        async with self.pinged:
            self.pinged.notify_all()

    async def expire(self):
        while True:
            async with self.pinged:
                await asyncio.wait_for(self.pinged.wait(), self.timeout)


@dataclasses.dataclass
class DatagramServer:
    connections: ConnectionManager
    config: dict
    gamepads: Mapping[int, DeviceBuffer] = dataclasses.field(default_factory=dict)
    clients: Mapping[str, DatagramClient] = dataclasses.field(default_factory=dict)
    send_count: int = 0
    recv_count: int = 0

    def __enter__(self):
        return self

    def __exit__(self, _type, _exc, _traceback):
        for gamepad in self.gamepads.values():
            gamepad.shm.unlink()

    async def handle_client(self, address: str, timeout: Real = None):
        """
        Create or keep alive a connection for a new client.
        """
        client = self.clients.get(address)
        if client:
            await client.keep_alive()
            client.timeout = client.timeout or timeout
        else:
            socket_config = {'socket_type': 'RADIO', 'address': address}
            client = self.clients[address] = DatagramClient(
                self.connections.open_connection(address, socket_config),
                timeout or self.config['client_timeout'],
            )
            LOGGER.debug('New datagram client connected', address=address)
            asyncio.create_task(self.expire(address, client))

    async def expire(self, address: str, client: DatagramClient):
        """ Watchdog timer for handling client timeouts. """
        try:
            await client.expire()
        except asyncio.TimeoutError:
            LOGGER.debug('Client timed out', address=address)
        finally:
            del self.clients[address]
            self.connections.close_connection(address)

    def get_gamepad_struct(self, gamepad_id: int):
        device_uid = f'gamepad-{gamepad_id}'
        if device_uid not in self.gamepads:
            device_type = get_device_type(protocol='dawn', device_name='Gamepad')
            self.gamepads[device_uid] = DeviceBuffer.open(device_type, device_uid, create=True)
            LOGGER.info('Initialized new gamepad', device_uid=device_uid)
        return self.gamepads[device_uid].struct

    async def update_gamepad_data(self, gamepad_id: int, gamepad_data):
        struct = self.get_gamepad_struct(gamepad_id)
        struct.set_current('joystick_left_x', gamepad_data.get('lx', 0))
        struct.set_current('joystick_left_y', gamepad_data.get('ly', 0))
        struct.set_current('joystick_right_x', gamepad_data.get('rx', 0))
        struct.set_current('joystick_right_y', gamepad_data.get('ry', 0))
        button_map = gamepad_data.get('btn', 0)
        gamepad_type = get_device_type(protocol='dawn', device_name='Gamepad')
        for i, param in enumerate(gamepad_type._params):
            if param.type == ctypes.c_bool:
                struct.set_current(param.name, bool((button_map >> i) & 0b1))

    async def recv_loop(self):
        while True:
            message = await self.connections.datagram_recv.recv()
            self.recv_count += 1
            try:
                address = message.get('src')
                if address:
                    await self.handle_client(address, message.get('timeout'))
                gamepads = message.get('gamepads') or {}
                for gamepad_id, gamepad in gamepads.items():
                    if 0 <= gamepad_id < self.config['max_gamepads']:
                        await self.update_gamepad_data(gamepad_id, gamepad)
                    else:
                        LOGGER.warn('Invalid gamepad ID', gamepad_id=gamepad_id,
                                    max_gamepads=self.config['max_gamepads'])
            except RuntimeBaseException as exc:
                LOGGER.warn('Encountered error while decoding datagram', exc=str(exc))

    async def broadcast(self):
        update = {}
        for client in self.clients.values():
            asyncio.create_task(client.conn.send(update))
            self.send_count += 1

    async def log_statistics(self):
        while True:
            await asyncio.sleep(self.config['log_interval'])
            bytes_sent = 0
            for client in self.clients.values():
                bytes_sent += client.conn.bytes_sent
                client.conn.bytes_sent = 0
            recv_conn = self.connections.datagram_recv
            LOGGER.info(
                'Datagram server statistics', clients=list(self.clients),
                send_count=self.send_count, recv_count=self.recv_count,
                bytes_sent=bytes_sent, bytes_recv=recv_conn.bytes_recv,
            )
            self.send_count, self.recv_count, recv_conn.bytes_recv = 0, 0, 0

    async def send_loop(self):
        loop = asyncio.get_running_loop()
        start, interval = loop.time(), self.config['send_interval']
        while True:
            try:
                start = loop.time()
                await asyncio.wait_for(self.broadcast(), interval)
                duration = loop.time() - start
                time_remaining = interval - duration
                if time_remaining > 0:
                    await asyncio.sleep(time_remaining)
            except asyncio.TimeoutError:
                LOGGER.warn('Send cycle timed out')

    async def broadcast_status(self):
        while True:
            devices = [buffer.status for buffer in self.gamepads.values()]
            await self.connections.gamepad_status.send({'devices': devices})
            await asyncio.sleep(self.config['broadcast_interval'])


@dataclasses.dataclass
class BrokerService(Service):
    config_schema = {
        **Service.config_schema,
        Optional('max_workers', default=5): POSITIVE_INTEGER,
        Optional('send_interval', default=0.05): POSITIVE_REAL,
        Optional('log_interval', default=30): POSITIVE_REAL,
        Optional('client_timeout', default=15): POSITIVE_REAL,
        Optional('broadcast_interval', default=1): POSITIVE_REAL,
        Optional('max_gamepads', default=4): POSITIVE_INTEGER,
        Optional('proxies', default={}): {
            VALID_NAME: {
                'frontend': VALID_NAME,
                'backend': VALID_NAME,
            }
        },
    }

    def serve_proxy(self, proxy):
        frontend, backend = proxy['frontend'], proxy['backend']
        frontend_socket = self.connections[frontend].socket
        backend_socket = self.connections[backend].socket
        LOGGER.debug('Serving proxy', frontend=frontend, backend=backend)
        # `zmq.proxy` is a C extension function, which `pylint` cannot detect.
        # pylint: disable=no-member
        zmq.proxy(frontend_socket, backend_socket)  # FIXME

    async def serve_proxies(self):
        with ThreadPoolExecutor(max_workers=self.config['max_workers']) as thread_pool:
            loop = asyncio.get_running_loop()
            proxies = [loop.run_in_executor(thread_pool, self.serve_proxy, proxy)
                       for proxy in self.config['proxies'].values()]
            await asyncio.wait(proxies)

    async def main(self):
        with DatagramServer(self.connections, self.config) as datagram_server:
            await asyncio.gather(
                self.serve_proxies(),
                datagram_server.recv_loop(),
                datagram_server.send_loop(),
                datagram_server.log_statistics(),
                datagram_server.broadcast_status(),
            )
