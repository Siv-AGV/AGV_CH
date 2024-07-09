// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from agv_msgs:srv/SetWheelSpeed.idl
// generated code does not contain a copyright notice

#ifndef AGV_MSGS__SRV__DETAIL__SET_WHEEL_SPEED__BUILDER_HPP_
#define AGV_MSGS__SRV__DETAIL__SET_WHEEL_SPEED__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "agv_msgs/srv/detail/set_wheel_speed__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace agv_msgs
{

namespace srv
{

namespace builder
{

class Init_SetWheelSpeed_Request_data
{
public:
  Init_SetWheelSpeed_Request_data()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::agv_msgs::srv::SetWheelSpeed_Request data(::agv_msgs::srv::SetWheelSpeed_Request::_data_type arg)
  {
    msg_.data = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_msgs::srv::SetWheelSpeed_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_msgs::srv::SetWheelSpeed_Request>()
{
  return agv_msgs::srv::builder::Init_SetWheelSpeed_Request_data();
}

}  // namespace agv_msgs


namespace agv_msgs
{

namespace srv
{

namespace builder
{

class Init_SetWheelSpeed_Response_message
{
public:
  Init_SetWheelSpeed_Response_message()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::agv_msgs::srv::SetWheelSpeed_Response message(::agv_msgs::srv::SetWheelSpeed_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_msgs::srv::SetWheelSpeed_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_msgs::srv::SetWheelSpeed_Response>()
{
  return agv_msgs::srv::builder::Init_SetWheelSpeed_Response_message();
}

}  // namespace agv_msgs

#endif  // AGV_MSGS__SRV__DETAIL__SET_WHEEL_SPEED__BUILDER_HPP_
