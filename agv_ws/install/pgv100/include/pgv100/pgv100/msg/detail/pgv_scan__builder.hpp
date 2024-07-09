// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from pgv100:msg/PGVScan.idl
// generated code does not contain a copyright notice

#ifndef PGV100__MSG__DETAIL__PGV_SCAN__BUILDER_HPP_
#define PGV100__MSG__DETAIL__PGV_SCAN__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "pgv100/msg/detail/pgv_scan__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace pgv100
{

namespace msg
{

namespace builder
{

class Init_PGVScan_tag_detected
{
public:
  explicit Init_PGVScan_tag_detected(::pgv100::msg::PGVScan & msg)
  : msg_(msg)
  {}
  ::pgv100::msg::PGVScan tag_detected(::pgv100::msg::PGVScan::_tag_detected_type arg)
  {
    msg_.tag_detected = std::move(arg);
    return std::move(msg_);
  }

private:
  ::pgv100::msg::PGVScan msg_;
};

class Init_PGVScan_no_position
{
public:
  explicit Init_PGVScan_no_position(::pgv100::msg::PGVScan & msg)
  : msg_(msg)
  {}
  Init_PGVScan_tag_detected no_position(::pgv100::msg::PGVScan::_no_position_type arg)
  {
    msg_.no_position = std::move(arg);
    return Init_PGVScan_tag_detected(msg_);
  }

private:
  ::pgv100::msg::PGVScan msg_;
};

class Init_PGVScan_no_color_lane
{
public:
  explicit Init_PGVScan_no_color_lane(::pgv100::msg::PGVScan & msg)
  : msg_(msg)
  {}
  Init_PGVScan_no_position no_color_lane(::pgv100::msg::PGVScan::_no_color_lane_type arg)
  {
    msg_.no_color_lane = std::move(arg);
    return Init_PGVScan_no_position(msg_);
  }

private:
  ::pgv100::msg::PGVScan msg_;
};

class Init_PGVScan_color_lane_count
{
public:
  explicit Init_PGVScan_color_lane_count(::pgv100::msg::PGVScan & msg)
  : msg_(msg)
  {}
  Init_PGVScan_no_color_lane color_lane_count(::pgv100::msg::PGVScan::_color_lane_count_type arg)
  {
    msg_.color_lane_count = std::move(arg);
    return Init_PGVScan_no_color_lane(msg_);
  }

private:
  ::pgv100::msg::PGVScan msg_;
};

class Init_PGVScan_direction
{
public:
  explicit Init_PGVScan_direction(::pgv100::msg::PGVScan & msg)
  : msg_(msg)
  {}
  Init_PGVScan_color_lane_count direction(::pgv100::msg::PGVScan::_direction_type arg)
  {
    msg_.direction = std::move(arg);
    return Init_PGVScan_color_lane_count(msg_);
  }

private:
  ::pgv100::msg::PGVScan msg_;
};

class Init_PGVScan_angle
{
public:
  explicit Init_PGVScan_angle(::pgv100::msg::PGVScan & msg)
  : msg_(msg)
  {}
  Init_PGVScan_direction angle(::pgv100::msg::PGVScan::_angle_type arg)
  {
    msg_.angle = std::move(arg);
    return Init_PGVScan_direction(msg_);
  }

private:
  ::pgv100::msg::PGVScan msg_;
};

class Init_PGVScan_y_position
{
public:
  explicit Init_PGVScan_y_position(::pgv100::msg::PGVScan & msg)
  : msg_(msg)
  {}
  Init_PGVScan_angle y_position(::pgv100::msg::PGVScan::_y_position_type arg)
  {
    msg_.y_position = std::move(arg);
    return Init_PGVScan_angle(msg_);
  }

private:
  ::pgv100::msg::PGVScan msg_;
};

class Init_PGVScan_x_position
{
public:
  explicit Init_PGVScan_x_position(::pgv100::msg::PGVScan & msg)
  : msg_(msg)
  {}
  Init_PGVScan_y_position x_position(::pgv100::msg::PGVScan::_x_position_type arg)
  {
    msg_.x_position = std::move(arg);
    return Init_PGVScan_y_position(msg_);
  }

private:
  ::pgv100::msg::PGVScan msg_;
};

class Init_PGVScan_header
{
public:
  Init_PGVScan_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PGVScan_x_position header(::pgv100::msg::PGVScan::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_PGVScan_x_position(msg_);
  }

private:
  ::pgv100::msg::PGVScan msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::pgv100::msg::PGVScan>()
{
  return pgv100::msg::builder::Init_PGVScan_header();
}

}  // namespace pgv100

#endif  // PGV100__MSG__DETAIL__PGV_SCAN__BUILDER_HPP_
