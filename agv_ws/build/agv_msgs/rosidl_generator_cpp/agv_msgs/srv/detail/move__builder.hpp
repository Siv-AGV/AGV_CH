// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from agv_msgs:srv/Move.idl
// generated code does not contain a copyright notice

#ifndef AGV_MSGS__SRV__DETAIL__MOVE__BUILDER_HPP_
#define AGV_MSGS__SRV__DETAIL__MOVE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "agv_msgs/srv/detail/move__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace agv_msgs
{

namespace srv
{

namespace builder
{

class Init_Move_Request_command
{
public:
  Init_Move_Request_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::agv_msgs::srv::Move_Request command(::agv_msgs::srv::Move_Request::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_msgs::srv::Move_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_msgs::srv::Move_Request>()
{
  return agv_msgs::srv::builder::Init_Move_Request_command();
}

}  // namespace agv_msgs


namespace agv_msgs
{

namespace srv
{

namespace builder
{

class Init_Move_Response_success
{
public:
  Init_Move_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::agv_msgs::srv::Move_Response success(::agv_msgs::srv::Move_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_msgs::srv::Move_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_msgs::srv::Move_Response>()
{
  return agv_msgs::srv::builder::Init_Move_Response_success();
}

}  // namespace agv_msgs

#endif  // AGV_MSGS__SRV__DETAIL__MOVE__BUILDER_HPP_
