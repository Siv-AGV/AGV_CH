// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from pgv100:msg/PGVScan.idl
// generated code does not contain a copyright notice

#ifndef PGV100__MSG__DETAIL__PGV_SCAN__STRUCT_H_
#define PGV100__MSG__DETAIL__PGV_SCAN__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'direction'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/PGVScan in the package pgv100.
typedef struct pgv100__msg__PGVScan
{
  std_msgs__msg__Header header;
  float x_position;
  float y_position;
  float angle;
  rosidl_runtime_c__String direction;
  uint8_t color_lane_count;
  uint8_t no_color_lane;
  uint8_t no_position;
  uint8_t tag_detected;
} pgv100__msg__PGVScan;

// Struct for a sequence of pgv100__msg__PGVScan.
typedef struct pgv100__msg__PGVScan__Sequence
{
  pgv100__msg__PGVScan * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} pgv100__msg__PGVScan__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PGV100__MSG__DETAIL__PGV_SCAN__STRUCT_H_
