// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from agv_msgs:srv/SetWheelSpeed.idl
// generated code does not contain a copyright notice

#ifndef AGV_MSGS__SRV__DETAIL__SET_WHEEL_SPEED__TRAITS_HPP_
#define AGV_MSGS__SRV__DETAIL__SET_WHEEL_SPEED__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "agv_msgs/srv/detail/set_wheel_speed__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace agv_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetWheelSpeed_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: data
  {
    out << "data: ";
    rosidl_generator_traits::value_to_yaml(msg.data, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetWheelSpeed_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: data
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "data: ";
    rosidl_generator_traits::value_to_yaml(msg.data, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetWheelSpeed_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace agv_msgs

namespace rosidl_generator_traits
{

[[deprecated("use agv_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const agv_msgs::srv::SetWheelSpeed_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  agv_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use agv_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const agv_msgs::srv::SetWheelSpeed_Request & msg)
{
  return agv_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<agv_msgs::srv::SetWheelSpeed_Request>()
{
  return "agv_msgs::srv::SetWheelSpeed_Request";
}

template<>
inline const char * name<agv_msgs::srv::SetWheelSpeed_Request>()
{
  return "agv_msgs/srv/SetWheelSpeed_Request";
}

template<>
struct has_fixed_size<agv_msgs::srv::SetWheelSpeed_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<agv_msgs::srv::SetWheelSpeed_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<agv_msgs::srv::SetWheelSpeed_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace agv_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetWheelSpeed_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: message
  {
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetWheelSpeed_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: message
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "message: ";
    rosidl_generator_traits::value_to_yaml(msg.message, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetWheelSpeed_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace agv_msgs

namespace rosidl_generator_traits
{

[[deprecated("use agv_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const agv_msgs::srv::SetWheelSpeed_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  agv_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use agv_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const agv_msgs::srv::SetWheelSpeed_Response & msg)
{
  return agv_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<agv_msgs::srv::SetWheelSpeed_Response>()
{
  return "agv_msgs::srv::SetWheelSpeed_Response";
}

template<>
inline const char * name<agv_msgs::srv::SetWheelSpeed_Response>()
{
  return "agv_msgs/srv/SetWheelSpeed_Response";
}

template<>
struct has_fixed_size<agv_msgs::srv::SetWheelSpeed_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<agv_msgs::srv::SetWheelSpeed_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<agv_msgs::srv::SetWheelSpeed_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<agv_msgs::srv::SetWheelSpeed>()
{
  return "agv_msgs::srv::SetWheelSpeed";
}

template<>
inline const char * name<agv_msgs::srv::SetWheelSpeed>()
{
  return "agv_msgs/srv/SetWheelSpeed";
}

template<>
struct has_fixed_size<agv_msgs::srv::SetWheelSpeed>
  : std::integral_constant<
    bool,
    has_fixed_size<agv_msgs::srv::SetWheelSpeed_Request>::value &&
    has_fixed_size<agv_msgs::srv::SetWheelSpeed_Response>::value
  >
{
};

template<>
struct has_bounded_size<agv_msgs::srv::SetWheelSpeed>
  : std::integral_constant<
    bool,
    has_bounded_size<agv_msgs::srv::SetWheelSpeed_Request>::value &&
    has_bounded_size<agv_msgs::srv::SetWheelSpeed_Response>::value
  >
{
};

template<>
struct is_service<agv_msgs::srv::SetWheelSpeed>
  : std::true_type
{
};

template<>
struct is_service_request<agv_msgs::srv::SetWheelSpeed_Request>
  : std::true_type
{
};

template<>
struct is_service_response<agv_msgs::srv::SetWheelSpeed_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // AGV_MSGS__SRV__DETAIL__SET_WHEEL_SPEED__TRAITS_HPP_
