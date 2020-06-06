# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pokemon.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pokemon.proto',
  package='echo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rpokemon.proto\x12\x04\x65\x63ho\"\"\n\x0ePokemonRequest\x12\x10\n\x08p_number\x18\x01 \x01(\x05\"F\n\x0fPokemonResponse\x12\x10\n\x08p_number\x18\x01 \x01(\x05\x12\x0e\n\x06p_name\x18\x02 \x01(\t\x12\x11\n\tp_species\x18\x03 \x01(\t2F\n\x07Pokemon\x12;\n\ngetPokemon\x12\x14.echo.PokemonRequest\x1a\x15.echo.PokemonResponse\"\x00\x62\x06proto3'
)




_POKEMONREQUEST = _descriptor.Descriptor(
  name='PokemonRequest',
  full_name='echo.PokemonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p_number', full_name='echo.PokemonRequest.p_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=23,
  serialized_end=57,
)


_POKEMONRESPONSE = _descriptor.Descriptor(
  name='PokemonResponse',
  full_name='echo.PokemonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p_number', full_name='echo.PokemonResponse.p_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p_name', full_name='echo.PokemonResponse.p_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p_species', full_name='echo.PokemonResponse.p_species', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=59,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['PokemonRequest'] = _POKEMONREQUEST
DESCRIPTOR.message_types_by_name['PokemonResponse'] = _POKEMONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokemonRequest = _reflection.GeneratedProtocolMessageType('PokemonRequest', (_message.Message,), {
  'DESCRIPTOR' : _POKEMONREQUEST,
  '__module__' : 'pokemon_pb2'
  # @@protoc_insertion_point(class_scope:echo.PokemonRequest)
  })
_sym_db.RegisterMessage(PokemonRequest)

PokemonResponse = _reflection.GeneratedProtocolMessageType('PokemonResponse', (_message.Message,), {
  'DESCRIPTOR' : _POKEMONRESPONSE,
  '__module__' : 'pokemon_pb2'
  # @@protoc_insertion_point(class_scope:echo.PokemonResponse)
  })
_sym_db.RegisterMessage(PokemonResponse)



_POKEMON = _descriptor.ServiceDescriptor(
  name='Pokemon',
  full_name='echo.Pokemon',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=131,
  serialized_end=201,
  methods=[
  _descriptor.MethodDescriptor(
    name='getPokemon',
    full_name='echo.Pokemon.getPokemon',
    index=0,
    containing_service=None,
    input_type=_POKEMONREQUEST,
    output_type=_POKEMONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_POKEMON)

DESCRIPTOR.services_by_name['Pokemon'] = _POKEMON

# @@protoc_insertion_point(module_scope)
