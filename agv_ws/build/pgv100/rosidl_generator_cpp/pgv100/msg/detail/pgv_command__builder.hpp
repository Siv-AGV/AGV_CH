// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pgv100:msg/PGVCommand.idl
// generated code does not contain a copyright notice

#ifndef PGV100__MSG__DETAIL__PGV_COMMAND__BUILDER_HPP_
#define PGV100__MSG__DETAIL__PGV_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pgv100/msg/detail/pgv_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pgv100
{

namespace msg
{

namespace builder
{

class Init_PGVCommand_command
{
public:
  Init_PGVCommand_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::pgv100::msg::PGVCommand command(::pgv100::msg::PGVCommand::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pgv100::msg::PGVCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::pgv100::msg::PGVCommand>()
{
  return pgv100::msg::builder::Init_PGVCommand_command();
}

}  // namespace pgv100

#endif  // PGV100__MSG__DETAIL__PGV_COMMAND__BUILDER_HPP_
