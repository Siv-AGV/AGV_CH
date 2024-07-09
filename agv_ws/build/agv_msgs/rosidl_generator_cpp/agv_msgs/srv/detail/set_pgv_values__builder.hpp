// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from agv_msgs:srv/SetPGVValues.idl
// generated code does not contain a copyright notice

#ifndef AGV_MSGS__SRV__DETAIL__SET_PGV_VALUES__BUILDER_HPP_
#define AGV_MSGS__SRV__DETAIL__SET_PGV_VALUES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "agv_msgs/srv/detail/set_pgv_values__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace agv_msgs
{

namespace srv
{

namespace builder
{

class Init_SetPGVValues_Request_z_offset
{
public:
  explicit Init_SetPGVValues_Request_z_offset(::agv_msgs::srv::SetPGVValues_Request & msg)
  : msg_(msg)
  {}
  ::agv_msgs::srv::SetPGVValues_Request z_offset(::agv_msgs::srv::SetPGVValues_Request::_z_offset_type arg)
  {
    msg_.z_offset = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_msgs::srv::SetPGVValues_Request msg_;
};

class Init_SetPGVValues_Request_y_offset
{
public:
  explicit Init_SetPGVValues_Request_y_offset(::agv_msgs::srv::SetPGVValues_Request & msg)
  : msg_(msg)
  {}
  Init_SetPGVValues_Request_z_offset y_offset(::agv_msgs::srv::SetPGVValues_Request::_y_offset_type arg)
  {
    msg_.y_offset = std::move(arg);
    return Init_SetPGVValues_Request_z_offset(msg_);
  }

private:
  ::agv_msgs::srv::SetPGVValues_Request msg_;
};

class Init_SetPGVValues_Request_x_offset
{
public:
  Init_SetPGVValues_Request_x_offset()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetPGVValues_Request_y_offset x_offset(::agv_msgs::srv::SetPGVValues_Request::_x_offset_type arg)
  {
    msg_.x_offset = std::move(arg);
    return Init_SetPGVValues_Request_y_offset(msg_);
  }

private:
  ::agv_msgs::srv::SetPGVValues_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_msgs::srv::SetPGVValues_Request>()
{
  return agv_msgs::srv::builder::Init_SetPGVValues_Request_x_offset();
}

}  // namespace agv_msgs


namespace agv_msgs
{

namespace srv
{

namespace builder
{

class Init_SetPGVValues_Response_message
{
public:
  explicit Init_SetPGVValues_Response_message(::agv_msgs::srv::SetPGVValues_Response & msg)
  : msg_(msg)
  {}
  ::agv_msgs::srv::SetPGVValues_Response message(::agv_msgs::srv::SetPGVValues_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_msgs::srv::SetPGVValues_Response msg_;
};

class Init_SetPGVValues_Response_success
{
public:
  Init_SetPGVValues_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetPGVValues_Response_message success(::agv_msgs::srv::SetPGVValues_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_SetPGVValues_Response_message(msg_);
  }

private:
  ::agv_msgs::srv::SetPGVValues_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_msgs::srv::SetPGVValues_Response>()
{
  return agv_msgs::srv::builder::Init_SetPGVValues_Response_success();
}

}  // namespace agv_msgs

#endif  // AGV_MSGS__SRV__DETAIL__SET_PGV_VALUES__BUILDER_HPP_
