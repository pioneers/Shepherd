# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gamepad.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gamepad.proto',
  package='',
  syntax='proto3',
  serialized_options=b'H\003',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rgamepad.proto\";\n\x07GpState\x12\x11\n\tconnected\x18\x01 \x01(\x08\x12\x0f\n\x07\x62uttons\x18\x02 \x01(\x07\x12\x0c\n\x04\x61xes\x18\x03 \x03(\x02\x42\x02H\x03\x62\x06proto3'
)




_GPSTATE = _descriptor.Descriptor(
  name='GpState',
  full_name='GpState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connected', full_name='GpState.connected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buttons', full_name='GpState.buttons', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='axes', full_name='GpState.axes', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=76,
)

DESCRIPTOR.message_types_by_name['GpState'] = _GPSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GpState = _reflection.GeneratedProtocolMessageType('GpState', (_message.Message,), {
  'DESCRIPTOR' : _GPSTATE,
  '__module__' : 'gamepad_pb2'
  # @@protoc_insertion_point(class_scope:GpState)
  })
_sym_db.RegisterMessage(GpState)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)