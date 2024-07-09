// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from pgv100:msg/PGVScan.idl
// generated code does not contain a copyright notice

#ifndef PGV100__MSG__DETAIL__PGV_SCAN__TRAITS_HPP_
#define PGV100__MSG__DETAIL__PGV_SCAN__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "pgv100/msg/detail/pgv_scan__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace pgv100
{

namespace msg
{

inline void to_flow_style_yaml(
  const PGVScan & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: x_position
  {
    out << "x_position: ";
    rosidl_generator_traits::value_to_yaml(msg.x_position, out);
    out << ", ";
  }

  // member: y_position
  {
    out << "y_position: ";
    rosidl_generator_traits::value_to_yaml(msg.y_position, out);
    out << ", ";
  }

  // member: angle
  {
    out << "angle: ";
    rosidl_generator_traits::value_to_yaml(msg.angle, out);
    out << ", ";
  }

  // member: direction
  {
    out << "direction: ";
    rosidl_generator_traits::value_to_yaml(msg.direction, out);
    out << ", ";
  }

  // member: color_lane_count
  {
    out << "color_lane_count: ";
    rosidl_generator_traits::value_to_yaml(msg.color_lane_count, out);
    out << ", ";
  }

  // member: no_color_lane
  {
    out << "no_color_lane: ";
    rosidl_generator_traits::value_to_yaml(msg.no_color_lane, out);
    out << ", ";
  }

  // member: no_position
  {
    out << "no_position: ";
    rosidl_generator_traits::value_to_yaml(msg.no_position, out);
    out << ", ";
  }

  // member: tag_detected
  {
    out << "tag_detected: ";
    rosidl_generator_traits::value_to_yaml(msg.tag_detected, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PGVScan & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: x_position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x_position: ";
    rosidl_generator_traits::value_to_yaml(msg.x_position, out);
    out << "\n";
  }

  // member: y_position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y_position: ";
    rosidl_generator_traits::value_to_yaml(msg.y_position, out);
    out << "\n";
  }

  // member: angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angle: ";
    rosidl_generator_traits::value_to_yaml(msg.angle, out);
    out << "\n";
  }

  // member: direction
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "direction: ";
    rosidl_generator_traits::value_to_yaml(msg.direction, out);
    out << "\n";
  }

  // member: color_lane_count
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "color_lane_count: ";
    rosidl_generator_traits::value_to_yaml(msg.color_lane_count, out);
    out << "\n";
  }

  // member: no_color_lane
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "no_color_lane: ";
    rosidl_generator_traits::value_to_yaml(msg.no_color_lane, out);
    out << "\n";
  }

  // member: no_position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "no_position: ";
    rosidl_generator_traits::value_to_yaml(msg.no_position, out);
    out << "\n";
  }

  // member: tag_detected
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "tag_detected: ";
    rosidl_generator_traits::value_to_yaml(msg.tag_detected, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PGVScan & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace pgv100

namespace rosidl_generator_traits
{

[[deprecated("use pgv100::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const pgv100::msg::PGVScan & msg,
  std::ostream & out, size_t indentation = 0)
{
  pgv100::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pgv100::msg::to_yaml() instead")]]
inline std::string to_yaml(const pgv100::msg::PGVScan & msg)
{
  return pgv100::msg::to_yaml(msg);
}

template<>
inline const char * data_type<pgv100::msg::PGVScan>()
{
  return "pgv100::msg::PGVScan";
}

template<>
inline const char * name<pgv100::msg::PGVScan>()
{
  return "pgv100/msg/PGVScan";
}

template<>
struct has_fixed_size<pgv100::msg::PGVScan>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<pgv100::msg::PGVScan>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<pgv100::msg::PGVScan>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PGV100__MSG__DETAIL__PGV_SCAN__TRAITS_HPP_
