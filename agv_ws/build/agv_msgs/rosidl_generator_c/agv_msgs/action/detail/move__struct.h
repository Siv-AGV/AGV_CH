// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from agv_msgs:action/Move.idl
// generated code does not contain a copyright notice

#ifndef AGV_MSGS__ACTION__DETAIL__MOVE__STRUCT_H_
#define AGV_MSGS__ACTION__DETAIL__MOVE__STRUCT_H_

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

/// Struct defined in action/Move in the package agv_msgs.
typedef struct agv_msgs__action__Move_Goal
{
  geometry_msgs__msg__Twist command;
} agv_msgs__action__Move_Goal;

// Struct for a sequence of agv_msgs__action__Move_Goal.
typedef struct agv_msgs__action__Move_Goal__Sequence
{
  agv_msgs__action__Move_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__action__Move_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/Move in the package agv_msgs.
typedef struct agv_msgs__action__Move_Result
{
  bool completed;
} agv_msgs__action__Move_Result;

// Struct for a sequence of agv_msgs__action__Move_Result.
typedef struct agv_msgs__action__Move_Result__Sequence
{
  agv_msgs__action__Move_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__action__Move_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/Move in the package agv_msgs.
typedef struct agv_msgs__action__Move_Feedback
{
  float current_distance;
  float current_angle;
} agv_msgs__action__Move_Feedback;

// Struct for a sequence of agv_msgs__action__Move_Feedback.
typedef struct agv_msgs__action__Move_Feedback__Sequence
{
  agv_msgs__action__Move_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__action__Move_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "agv_msgs/action/detail/move__struct.h"

/// Struct defined in action/Move in the package agv_msgs.
typedef struct agv_msgs__action__Move_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  agv_msgs__action__Move_Goal goal;
} agv_msgs__action__Move_SendGoal_Request;

// Struct for a sequence of agv_msgs__action__Move_SendGoal_Request.
typedef struct agv_msgs__action__Move_SendGoal_Request__Sequence
{
  agv_msgs__action__Move_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__action__Move_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/Move in the package agv_msgs.
typedef struct agv_msgs__action__Move_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} agv_msgs__action__Move_SendGoal_Response;

// Struct for a sequence of agv_msgs__action__Move_SendGoal_Response.
typedef struct agv_msgs__action__Move_SendGoal_Response__Sequence
{
  agv_msgs__action__Move_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__action__Move_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/Move in the package agv_msgs.
typedef struct agv_msgs__action__Move_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} agv_msgs__action__Move_GetResult_Request;

// Struct for a sequence of agv_msgs__action__Move_GetResult_Request.
typedef struct agv_msgs__action__Move_GetResult_Request__Sequence
{
  agv_msgs__action__Move_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__action__Move_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "agv_msgs/action/detail/move__struct.h"

/// Struct defined in action/Move in the package agv_msgs.
typedef struct agv_msgs__action__Move_GetResult_Response
{
  int8_t status;
  agv_msgs__action__Move_Result result;
} agv_msgs__action__Move_GetResult_Response;

// Struct for a sequence of agv_msgs__action__Move_GetResult_Response.
typedef struct agv_msgs__action__Move_GetResult_Response__Sequence
{
  agv_msgs__action__Move_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__action__Move_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "agv_msgs/action/detail/move__struct.h"

/// Struct defined in action/Move in the package agv_msgs.
typedef struct agv_msgs__action__Move_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  agv_msgs__action__Move_Feedback feedback;
} agv_msgs__action__Move_FeedbackMessage;

// Struct for a sequence of agv_msgs__action__Move_FeedbackMessage.
typedef struct agv_msgs__action__Move_FeedbackMessage__Sequence
{
  agv_msgs__action__Move_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} agv_msgs__action__Move_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AGV_MSGS__ACTION__DETAIL__MOVE__STRUCT_H_
