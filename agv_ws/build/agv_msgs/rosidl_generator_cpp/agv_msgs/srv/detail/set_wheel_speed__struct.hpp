// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from agv_msgs:srv/SetWheelSpeed.idl
// generated code does not contain a copyright notice

#ifndef AGV_MSGS__SRV__DETAIL__SET_WHEEL_SPEED__STRUCT_HPP_
#define AGV_MSGS__SRV__DETAIL__SET_WHEEL_SPEED__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__agv_msgs__srv__SetWheelSpeed_Request __attribute__((deprecated))
#else
# define DEPRECATED__agv_msgs__srv__SetWheelSpeed_Request __declspec(deprecated)
#endif

namespace agv_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetWheelSpeed_Request_
{
  using Type = SetWheelSpeed_Request_<ContainerAllocator>;

  explicit SetWheelSpeed_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = 0.0;
    }
  }

  explicit SetWheelSpeed_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->data = 0.0;
    }
  }

  // field types and members
  using _data_type =
    double;
  _data_type data;

  // setters for named parameter idiom
  Type & set__data(
    const double & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__agv_msgs__srv__SetWheelSpeed_Request
    std::shared_ptr<agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__agv_msgs__srv__SetWheelSpeed_Request
    std::shared_ptr<agv_msgs::srv::SetWheelSpeed_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetWheelSpeed_Request_ & other) const
  {
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetWheelSpeed_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetWheelSpeed_Request_

// alias to use template instance with default allocator
using SetWheelSpeed_Request =
  agv_msgs::srv::SetWheelSpeed_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace agv_msgs


#ifndef _WIN32
# define DEPRECATED__agv_msgs__srv__SetWheelSpeed_Response __attribute__((deprecated))
#else
# define DEPRECATED__agv_msgs__srv__SetWheelSpeed_Response __declspec(deprecated)
#endif

namespace agv_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetWheelSpeed_Response_
{
  using Type = SetWheelSpeed_Response_<ContainerAllocator>;

  explicit SetWheelSpeed_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->message = "";
    }
  }

  explicit SetWheelSpeed_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : message(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->message = "";
    }
  }

  // field types and members
  using _message_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _message_type message;

  // setters for named parameter idiom
  Type & set__message(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->message = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__agv_msgs__srv__SetWheelSpeed_Response
    std::shared_ptr<agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__agv_msgs__srv__SetWheelSpeed_Response
    std::shared_ptr<agv_msgs::srv::SetWheelSpeed_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetWheelSpeed_Response_ & other) const
  {
    if (this->message != other.message) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetWheelSpeed_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetWheelSpeed_Response_

// alias to use template instance with default allocator
using SetWheelSpeed_Response =
  agv_msgs::srv::SetWheelSpeed_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace agv_msgs

namespace agv_msgs
{

namespace srv
{

struct SetWheelSpeed
{
  using Request = agv_msgs::srv::SetWheelSpeed_Request;
  using Response = agv_msgs::srv::SetWheelSpeed_Response;
};

}  // namespace srv

}  // namespace agv_msgs

#endif  // AGV_MSGS__SRV__DETAIL__SET_WHEEL_SPEED__STRUCT_HPP_
