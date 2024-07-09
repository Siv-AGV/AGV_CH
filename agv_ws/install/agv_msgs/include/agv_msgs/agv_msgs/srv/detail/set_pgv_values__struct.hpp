// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from agv_msgs:srv/SetPGVValues.idl
// generated code does not contain a copyright notice

#ifndef AGV_MSGS__SRV__DETAIL__SET_PGV_VALUES__STRUCT_HPP_
#define AGV_MSGS__SRV__DETAIL__SET_PGV_VALUES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__agv_msgs__srv__SetPGVValues_Request __attribute__((deprecated))
#else
# define DEPRECATED__agv_msgs__srv__SetPGVValues_Request __declspec(deprecated)
#endif

namespace agv_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetPGVValues_Request_
{
  using Type = SetPGVValues_Request_<ContainerAllocator>;

  explicit SetPGVValues_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x_offset = 0.0;
      this->y_offset = 0.0;
      this->z_offset = 0.0;
    }
  }

  explicit SetPGVValues_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x_offset = 0.0;
      this->y_offset = 0.0;
      this->z_offset = 0.0;
    }
  }

  // field types and members
  using _x_offset_type =
    double;
  _x_offset_type x_offset;
  using _y_offset_type =
    double;
  _y_offset_type y_offset;
  using _z_offset_type =
    double;
  _z_offset_type z_offset;

  // setters for named parameter idiom
  Type & set__x_offset(
    const double & _arg)
  {
    this->x_offset = _arg;
    return *this;
  }
  Type & set__y_offset(
    const double & _arg)
  {
    this->y_offset = _arg;
    return *this;
  }
  Type & set__z_offset(
    const double & _arg)
  {
    this->z_offset = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__agv_msgs__srv__SetPGVValues_Request
    std::shared_ptr<agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__agv_msgs__srv__SetPGVValues_Request
    std::shared_ptr<agv_msgs::srv::SetPGVValues_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetPGVValues_Request_ & other) const
  {
    if (this->x_offset != other.x_offset) {
      return false;
    }
    if (this->y_offset != other.y_offset) {
      return false;
    }
    if (this->z_offset != other.z_offset) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetPGVValues_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetPGVValues_Request_

// alias to use template instance with default allocator
using SetPGVValues_Request =
  agv_msgs::srv::SetPGVValues_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace agv_msgs


#ifndef _WIN32
# define DEPRECATED__agv_msgs__srv__SetPGVValues_Response __attribute__((deprecated))
#else
# define DEPRECATED__agv_msgs__srv__SetPGVValues_Response __declspec(deprecated)
#endif

namespace agv_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetPGVValues_Response_
{
  using Type = SetPGVValues_Response_<ContainerAllocator>;

  explicit SetPGVValues_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  explicit SetPGVValues_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->message = "";
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__agv_msgs__srv__SetPGVValues_Response
    std::shared_ptr<agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__agv_msgs__srv__SetPGVValues_Response
    std::shared_ptr<agv_msgs::srv::SetPGVValues_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetPGVValues_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetPGVValues_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetPGVValues_Response_

// alias to use template instance with default allocator
using SetPGVValues_Response =
  agv_msgs::srv::SetPGVValues_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace agv_msgs

namespace agv_msgs
{

namespace srv
{

struct SetPGVValues
{
  using Request = agv_msgs::srv::SetPGVValues_Request;
  using Response = agv_msgs::srv::SetPGVValues_Response;
};

}  // namespace srv

}  // namespace agv_msgs

#endif  // AGV_MSGS__SRV__DETAIL__SET_PGV_VALUES__STRUCT_HPP_
