// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from agv_msgs:srv/Move.idl
// generated code does not contain a copyright notice

#ifndef AGV_MSGS__SRV__DETAIL__MOVE__STRUCT_HPP_
#define AGV_MSGS__SRV__DETAIL__MOVE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'command'
#include "geometry_msgs/msg/detail/twist__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__agv_msgs__srv__Move_Request __attribute__((deprecated))
#else
# define DEPRECATED__agv_msgs__srv__Move_Request __declspec(deprecated)
#endif

namespace agv_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Move_Request_
{
  using Type = Move_Request_<ContainerAllocator>;

  explicit Move_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_init)
  {
    (void)_init;
  }

  explicit Move_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _command_type =
    geometry_msgs::msg::Twist_<ContainerAllocator>;
  _command_type command;

  // setters for named parameter idiom
  Type & set__command(
    const geometry_msgs::msg::Twist_<ContainerAllocator> & _arg)
  {
    this->command = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    agv_msgs::srv::Move_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const agv_msgs::srv::Move_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<agv_msgs::srv::Move_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<agv_msgs::srv::Move_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::Move_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::Move_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::Move_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::Move_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<agv_msgs::srv::Move_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<agv_msgs::srv::Move_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__agv_msgs__srv__Move_Request
    std::shared_ptr<agv_msgs::srv::Move_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__agv_msgs__srv__Move_Request
    std::shared_ptr<agv_msgs::srv::Move_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Move_Request_ & other) const
  {
    if (this->command != other.command) {
      return false;
    }
    return true;
  }
  bool operator!=(const Move_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Move_Request_

// alias to use template instance with default allocator
using Move_Request =
  agv_msgs::srv::Move_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace agv_msgs


#ifndef _WIN32
# define DEPRECATED__agv_msgs__srv__Move_Response __attribute__((deprecated))
#else
# define DEPRECATED__agv_msgs__srv__Move_Response __declspec(deprecated)
#endif

namespace agv_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Move_Response_
{
  using Type = Move_Response_<ContainerAllocator>;

  explicit Move_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit Move_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    agv_msgs::srv::Move_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const agv_msgs::srv::Move_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<agv_msgs::srv::Move_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<agv_msgs::srv::Move_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::Move_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::Move_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      agv_msgs::srv::Move_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<agv_msgs::srv::Move_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<agv_msgs::srv::Move_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<agv_msgs::srv::Move_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__agv_msgs__srv__Move_Response
    std::shared_ptr<agv_msgs::srv::Move_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__agv_msgs__srv__Move_Response
    std::shared_ptr<agv_msgs::srv::Move_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Move_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const Move_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Move_Response_

// alias to use template instance with default allocator
using Move_Response =
  agv_msgs::srv::Move_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace agv_msgs

namespace agv_msgs
{

namespace srv
{

struct Move
{
  using Request = agv_msgs::srv::Move_Request;
  using Response = agv_msgs::srv::Move_Response;
};

}  // namespace srv

}  // namespace agv_msgs

#endif  // AGV_MSGS__SRV__DETAIL__MOVE__STRUCT_HPP_
