// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from agv_msgs:srv/SetPGVValues.idl
// generated code does not contain a copyright notice

#ifndef AGV_MSGS__SRV__DETAIL__SET_PGV_VALUES__STRUCT_H_
#define AGV_MSGS__SRV__DETAIL__SET_PGV_VALUES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/SetPGVValues in the package agv_msgs.
typedef struct agv_msgs__srv__SetPGVValues_Request
{
  double x_offset;
  double y_offset;
  double z_offset;
} agv_msgs__srv__SetPGVValues_Request;

// Struct for a sequence of agv_msgs__srv__SetPGVValues_Request.
typedef struct agv_msgs__srv__SetPGVValues_Request__Sequence
{
  agv_msgs__srv__SetPGVValues_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__srv__SetPGVValues_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/SetPGVValues in the package agv_msgs.
typedef struct agv_msgs__srv__SetPGVValues_Response
{
  bool success;
  rosidl_runtime_c__String message;
} agv_msgs__srv__SetPGVValues_Response;

// Struct for a sequence of agv_msgs__srv__SetPGVValues_Response.
typedef struct agv_msgs__srv__SetPGVValues_Response__Sequence
{
  agv_msgs__srv__SetPGVValues_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__srv__SetPGVValues_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AGV_MSGS__SRV__DETAIL__SET_PGV_VALUES__STRUCT_H_
