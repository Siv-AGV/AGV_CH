// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from pgv100:msg/PGVCommand.idl
// generated code does not contain a copyright notice

#ifndef PGV100__MSG__DETAIL__PGV_COMMAND__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define PGV100__MSG__DETAIL__PGV_COMMAND__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "pgv100/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "pgv100/msg/detail/pgv_command__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace pgv100
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pgv100
cdr_serialize(
  const pgv100::msg::PGVCommand & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pgv100
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  pgv100::msg::PGVCommand & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pgv100
get_serialized_size(
  const pgv100::msg::PGVCommand & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pgv100
max_serialized_size_PGVCommand(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace pgv100

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_pgv100
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, pgv100, msg, PGVCommand)();

#ifdef __cplusplus
}
#endif

#endif  // PGV100__MSG__DETAIL__PGV_COMMAND__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
