// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from pgv100:msg/PGVCommand.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "pgv100/msg/detail/pgv_command__rosidl_typesupport_introspection_c.h"
#include "pgv100/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "pgv100/msg/detail/pgv_command__functions.h"
#include "pgv100/msg/detail/pgv_command__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  pgv100__msg__PGVCommand__init(message_memory);
}

void pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_fini_function(void * message_memory)
{
  pgv100__msg__PGVCommand__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_message_member_array[1] = {
  {
    "command",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(pgv100__msg__PGVCommand, command),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_message_members = {
  "pgv100__msg",  // message namespace
  "PGVCommand",  // message name
  1,  // number of fields
  sizeof(pgv100__msg__PGVCommand),
  pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_message_member_array,  // message members
  pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_init_function,  // function to initialize message memory (memory has to be allocated)
  pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_message_type_support_handle = {
  0,
  &pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_pgv100
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, pgv100, msg, PGVCommand)() {
  if (!pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_message_type_support_handle.typesupport_identifier) {
    pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &pgv100__msg__PGVCommand__rosidl_typesupport_introspection_c__PGVCommand_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
