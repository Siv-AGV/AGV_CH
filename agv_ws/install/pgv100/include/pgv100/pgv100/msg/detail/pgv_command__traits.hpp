// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from pgv100:msg/PGVCommand.idl
// generated code does not contain a copyright notice

#ifndef PGV100__MSG__DETAIL__PGV_COMMAND__TRAITS_HPP_
#define PGV100__MSG__DETAIL__PGV_COMMAND__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "pgv100/msg/detail/pgv_command__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace pgv100
{

namespace msg
{

inline void to_flow_style_yaml(
  const PGVCommand & msg,
  std::ostream & out)
{
  out << "{";
  // member: command
  {
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PGVCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: command
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "command: ";
    rosidl_generator_traits::value_to_yaml(msg.command, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PGVCommand & msg, bool use_flow_style = false)
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
  const pgv100::msg::PGVCommand & msg,
  std::ostream & out, size_t indentation = 0)
{
  pgv100::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use pgv100::msg::to_yaml() instead")]]
inline std::string to_yaml(const pgv100::msg::PGVCommand & msg)
{
  return pgv100::msg::to_yaml(msg);
}

template<>
inline const char * data_type<pgv100::msg::PGVCommand>()
{
  return "pgv100::msg::PGVCommand";
}

template<>
inline const char * name<pgv100::msg::PGVCommand>()
{
  return "pgv100/msg/PGVCommand";
}

template<>
struct has_fixed_size<pgv100::msg::PGVCommand>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<pgv100::msg::PGVCommand>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<pgv100::msg::PGVCommand>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PGV100__MSG__DETAIL__PGV_COMMAND__TRAITS_HPP_
