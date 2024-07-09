// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from pgv100:msg/PGVScan.idl
// generated code does not contain a copyright notice

#ifndef PGV100__MSG__DETAIL__PGV_SCAN__STRUCT_HPP_
#define PGV100__MSG__DETAIL__PGV_SCAN__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__pgv100__msg__PGVScan __attribute__((deprecated))
#else
# define DEPRECATED__pgv100__msg__PGVScan __declspec(deprecated)
#endif

namespace pgv100
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PGVScan_
{
  using Type = PGVScan_<ContainerAllocator>;

  explicit PGVScan_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x_position = 0.0f;
      this->y_position = 0.0f;
      this->angle = 0.0f;
      this->direction = "";
      this->color_lane_count = 0;
      this->no_color_lane = 0;
      this->no_position = 0;
      this->tag_detected = 0;
    }
  }

  explicit PGVScan_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    direction(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x_position = 0.0f;
      this->y_position = 0.0f;
      this->angle = 0.0f;
      this->direction = "";
      this->color_lane_count = 0;
      this->no_color_lane = 0;
      this->no_position = 0;
      this->tag_detected = 0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _x_position_type =
    float;
  _x_position_type x_position;
  using _y_position_type =
    float;
  _y_position_type y_position;
  using _angle_type =
    float;
  _angle_type angle;
  using _direction_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _direction_type direction;
  using _color_lane_count_type =
    uint8_t;
  _color_lane_count_type color_lane_count;
  using _no_color_lane_type =
    uint8_t;
  _no_color_lane_type no_color_lane;
  using _no_position_type =
    uint8_t;
  _no_position_type no_position;
  using _tag_detected_type =
    uint8_t;
  _tag_detected_type tag_detected;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__x_position(
    const float & _arg)
  {
    this->x_position = _arg;
    return *this;
  }
  Type & set__y_position(
    const float & _arg)
  {
    this->y_position = _arg;
    return *this;
  }
  Type & set__angle(
    const float & _arg)
  {
    this->angle = _arg;
    return *this;
  }
  Type & set__direction(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->direction = _arg;
    return *this;
  }
  Type & set__color_lane_count(
    const uint8_t & _arg)
  {
    this->color_lane_count = _arg;
    return *this;
  }
  Type & set__no_color_lane(
    const uint8_t & _arg)
  {
    this->no_color_lane = _arg;
    return *this;
  }
  Type & set__no_position(
    const uint8_t & _arg)
  {
    this->no_position = _arg;
    return *this;
  }
  Type & set__tag_detected(
    const uint8_t & _arg)
  {
    this->tag_detected = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pgv100::msg::PGVScan_<ContainerAllocator> *;
  using ConstRawPtr =
    const pgv100::msg::PGVScan_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pgv100::msg::PGVScan_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pgv100::msg::PGVScan_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pgv100::msg::PGVScan_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pgv100::msg::PGVScan_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pgv100::msg::PGVScan_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pgv100::msg::PGVScan_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pgv100::msg::PGVScan_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pgv100::msg::PGVScan_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pgv100__msg__PGVScan
    std::shared_ptr<pgv100::msg::PGVScan_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pgv100__msg__PGVScan
    std::shared_ptr<pgv100::msg::PGVScan_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PGVScan_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->x_position != other.x_position) {
      return false;
    }
    if (this->y_position != other.y_position) {
      return false;
    }
    if (this->angle != other.angle) {
      return false;
    }
    if (this->direction != other.direction) {
      return false;
    }
    if (this->color_lane_count != other.color_lane_count) {
      return false;
    }
    if (this->no_color_lane != other.no_color_lane) {
      return false;
    }
    if (this->no_position != other.no_position) {
      return false;
    }
    if (this->tag_detected != other.tag_detected) {
      return false;
    }
    return true;
  }
  bool operator!=(const PGVScan_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PGVScan_

// alias to use template instance with default allocator
using PGVScan =
  pgv100::msg::PGVScan_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace pgv100

#endif  // PGV100__MSG__DETAIL__PGV_SCAN__STRUCT_HPP_
