# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: start_pos.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='start_pos.proto',
  package='',
  syntax='proto3',
  serialized_options=b'H\003',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fstart_pos.proto\"\x1d\n\x08StartPos\x12\x11\n\x03pos\x18\x01 \x01(\x0e\x32\x04.Pos*\x1a\n\x03Pos\x12\x08\n\x04LEFT\x10\x00\x12\t\n\x05RIGHT\x10\x01\x42\x02H\x03\x62\x06proto3'
)

_POS = _descriptor.EnumDescriptor(
  name='Pos',
  full_name='Pos',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LEFT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RIGHT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=50,
  serialized_end=76,
)
_sym_db.RegisterEnumDescriptor(_POS)

Pos = enum_type_wrapper.EnumTypeWrapper(_POS)
LEFT = 0
RIGHT = 1



_STARTPOS = _descriptor.Descriptor(
  name='StartPos',
  full_name='StartPos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos', full_name='StartPos.pos', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=19,
  serialized_end=48,
)

_STARTPOS.fields_by_name['pos'].enum_type = _POS
DESCRIPTOR.message_types_by_name['StartPos'] = _STARTPOS
DESCRIPTOR.enum_types_by_name['Pos'] = _POS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StartPos = _reflection.GeneratedProtocolMessageType('StartPos', (_message.Message,), {
  'DESCRIPTOR' : _STARTPOS,
  '__module__' : 'start_pos_pb2'
  # @@protoc_insertion_point(class_scope:StartPos)
  })
_sym_db.RegisterMessage(StartPos)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)