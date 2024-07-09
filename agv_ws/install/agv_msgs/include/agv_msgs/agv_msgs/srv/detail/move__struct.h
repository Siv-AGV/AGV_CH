// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from agv_msgs:srv/Move.idl
// generated code does not contain a copyright notice

#ifndef AGV_MSGS__SRV__DETAIL__MOVE__STRUCT_H_
#define AGV_MSGS__SRV__DETAIL__MOVE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'command'
#include "geometry_msgs/msg/detail/twist__struct.h"

/// Struct defined in srv/Move in the package agv_msgs.
typedef struct agv_msgs__srv__Move_Request
{
  geometry_msgs__msg__Twist command;
} agv_msgs__srv__Move_Request;

// Struct for a sequence of agv_msgs__srv__Move_Request.
typedef struct agv_msgs__srv__Move_Request__Sequence
{
  agv_msgs__srv__Move_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__srv__Move_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Move in the package agv_msgs.
typedef struct agv_msgs__srv__Move_Response
{
  bool success;
} agv_msgs__srv__Move_Response;

// Struct for a sequence of agv_msgs__srv__Move_Response.
typedef struct agv_msgs__srv__Move_Response__Sequence
{
  agv_msgs__srv__Move_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__srv__Move_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AGV_MSGS__SRV__DETAIL__MOVE__STRUCT_H_
