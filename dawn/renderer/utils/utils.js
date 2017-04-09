export const TIMEOUT = 5000;

export const pathToName = (filepath) => {
  if (filepath !== null) {
    if (process.platform === 'win32') {
      return filepath.split('\\').pop();
    }
    return filepath.split('/').pop();
  }
  return false;
};

const IPV4_REGEX = /^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}$/;
export const getValidationState = (testIPAddress) => {
  if (IPV4_REGEX.test(testIPAddress)) {
    return 'success';
  }
  if (testIPAddress === 'localhost') {
    return 'warning';
  }
  return 'error';
};

export const uploadStatus = {
  RECEIVED: 0,
  SENT: 1,
  ERROR: 2,
};

export const robotState = {
  IDLE: 0,
  SIMSTR: 'Simulation',
  TELEOP: 1,
  TELEOPSTR: 'Tele-Operated',
  AUTONOMOUS: 2,
  AUTOSTR: 'Autonomous',
  ESTOP: 3,
  ESTOPSTR: 'ESTOP',
};

// TODO: Synchronize this and the above state
export const runtimeState = {
  STUDENT_CRASHED: 0,
  0: 'Crashed',
  STUDENT_RUNNING: 1,
  1: 'Running',
  STUDENT_STOPPED: 2,
  2: 'Stopped',
  TELEOP: 3,
  3: 'Tele-Operated',
  AUTONOMOUS: 4,
  4: 'Autonomous',
  ESTOP: 5,
  5: 'E-Stop',
};

export const defaults = {
  PORT: 22,
  USERNAME: 'ubuntu',
  PASSWORD: 'temppwd',
  IPADDRESS: '192.168.7.2',
};

export const timings = {
  AUTO: 30,
  IDLE: 5,
  TELEOP: 120,
  SEC: 1000,
};
