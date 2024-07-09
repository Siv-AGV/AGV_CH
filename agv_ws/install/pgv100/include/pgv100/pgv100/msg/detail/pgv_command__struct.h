// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pgv100:msg/PGVCommand.idl
// generated code does not contain a copyright notice

#ifndef PGV100__MSG__DETAIL__PGV_COMMAND__STRUCT_H_
#define PGV100__MSG__DETAIL__PGV_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/PGVCommand in the package pgv100.
typedef struct pgv100__msg__PGVCommand
{
  uint8_t command;
} pgv100__msg__PGVCommand;

// Struct for a sequence of pgv100__msg__PGVCommand.
typedef struct pgv100__msg__PGVCommand__Sequence
{
  pgv100__msg__PGVCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pgv100__msg__PGVCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PGV100__MSG__DETAIL__PGV_COMMAND__STRUCT_H_
