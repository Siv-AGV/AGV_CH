// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from pgv100:msg/PGVCommand.idl
// generated code does not contain a copyright notice

#ifndef PGV100__MSG__DETAIL__PGV_COMMAND__STRUCT_HPP_
#define PGV100__MSG__DETAIL__PGV_COMMAND__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__pgv100__msg__PGVCommand __attribute__((deprecated))
#else
# define DEPRECATED__pgv100__msg__PGVCommand __declspec(deprecated)
#endif

namespace pgv100
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PGVCommand_
{
  using Type = PGVCommand_<ContainerAllocator>;

  explicit PGVCommand_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command = 0;
    }
  }

  explicit PGVCommand_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command = 0;
    }
  }

  // field types and members
  using _command_type =
    uint8_t;
  _command_type command;

  // setters for named parameter idiom
  Type & set__command(
    const uint8_t & _arg)
  {
    this->command = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    pgv100::msg::PGVCommand_<ContainerAllocator> *;
  using ConstRawPtr =
    const pgv100::msg::PGVCommand_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<pgv100::msg::PGVCommand_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<pgv100::msg::PGVCommand_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      pgv100::msg::PGVCommand_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<pgv100::msg::PGVCommand_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      pgv100::msg::PGVCommand_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<pgv100::msg::PGVCommand_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<pgv100::msg::PGVCommand_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<pgv100::msg::PGVCommand_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__pgv100__msg__PGVCommand
    std::shared_ptr<pgv100::msg::PGVCommand_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__pgv100__msg__PGVCommand
    std::shared_ptr<pgv100::msg::PGVCommand_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PGVCommand_ & other) const
  {
    if (this->command != other.command) {
      return false;
    }
    return true;
  }
  bool operator!=(const PGVCommand_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PGVCommand_

// alias to use template instance with default allocator
using PGVCommand =
  pgv100::msg::PGVCommand_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace pgv100

#endif  // PGV100__MSG__DETAIL__PGV_COMMAND__STRUCT_HPP_
