// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from agv_controller:action/Move.idl
// generated code does not contain a copyright notice

#ifndef AGV_CONTROLLER__ACTION__DETAIL__MOVE__BUILDER_HPP_
#define AGV_CONTROLLER__ACTION__DETAIL__MOVE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "agv_controller/action/detail/move__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace agv_controller
{

namespace action
{

namespace builder
{

class Init_Move_Goal_command
{
public:
  Init_Move_Goal_command()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::agv_controller::action::Move_Goal command(::agv_controller::action::Move_Goal::_command_type arg)
  {
    msg_.command = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_controller::action::Move_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_controller::action::Move_Goal>()
{
  return agv_controller::action::builder::Init_Move_Goal_command();
}

}  // namespace agv_controller


namespace agv_controller
{

namespace action
{

namespace builder
{

class Init_Move_Result_completed
{
public:
  Init_Move_Result_completed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::agv_controller::action::Move_Result completed(::agv_controller::action::Move_Result::_completed_type arg)
  {
    msg_.completed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_controller::action::Move_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_controller::action::Move_Result>()
{
  return agv_controller::action::builder::Init_Move_Result_completed();
}

}  // namespace agv_controller


namespace agv_controller
{

namespace action
{

namespace builder
{

class Init_Move_Feedback_current_angle
{
public:
  explicit Init_Move_Feedback_current_angle(::agv_controller::action::Move_Feedback & msg)
  : msg_(msg)
  {}
  ::agv_controller::action::Move_Feedback current_angle(::agv_controller::action::Move_Feedback::_current_angle_type arg)
  {
    msg_.current_angle = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_controller::action::Move_Feedback msg_;
};

class Init_Move_Feedback_current_distance
{
public:
  Init_Move_Feedback_current_distance()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_Feedback_current_angle current_distance(::agv_controller::action::Move_Feedback::_current_distance_type arg)
  {
    msg_.current_distance = std::move(arg);
    return Init_Move_Feedback_current_angle(msg_);
  }

private:
  ::agv_controller::action::Move_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_controller::action::Move_Feedback>()
{
  return agv_controller::action::builder::Init_Move_Feedback_current_distance();
}

}  // namespace agv_controller


namespace agv_controller
{

namespace action
{

namespace builder
{

class Init_Move_SendGoal_Request_goal
{
public:
  explicit Init_Move_SendGoal_Request_goal(::agv_controller::action::Move_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::agv_controller::action::Move_SendGoal_Request goal(::agv_controller::action::Move_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_controller::action::Move_SendGoal_Request msg_;
};

class Init_Move_SendGoal_Request_goal_id
{
public:
  Init_Move_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_SendGoal_Request_goal goal_id(::agv_controller::action::Move_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Move_SendGoal_Request_goal(msg_);
  }

private:
  ::agv_controller::action::Move_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_controller::action::Move_SendGoal_Request>()
{
  return agv_controller::action::builder::Init_Move_SendGoal_Request_goal_id();
}

}  // namespace agv_controller


namespace agv_controller
{

namespace action
{

namespace builder
{

class Init_Move_SendGoal_Response_stamp
{
public:
  explicit Init_Move_SendGoal_Response_stamp(::agv_controller::action::Move_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::agv_controller::action::Move_SendGoal_Response stamp(::agv_controller::action::Move_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_controller::action::Move_SendGoal_Response msg_;
};

class Init_Move_SendGoal_Response_accepted
{
public:
  Init_Move_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_SendGoal_Response_stamp accepted(::agv_controller::action::Move_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Move_SendGoal_Response_stamp(msg_);
  }

private:
  ::agv_controller::action::Move_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_controller::action::Move_SendGoal_Response>()
{
  return agv_controller::action::builder::Init_Move_SendGoal_Response_accepted();
}

}  // namespace agv_controller


namespace agv_controller
{

namespace action
{

namespace builder
{

class Init_Move_GetResult_Request_goal_id
{
public:
  Init_Move_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::agv_controller::action::Move_GetResult_Request goal_id(::agv_controller::action::Move_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_controller::action::Move_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_controller::action::Move_GetResult_Request>()
{
  return agv_controller::action::builder::Init_Move_GetResult_Request_goal_id();
}

}  // namespace agv_controller


namespace agv_controller
{

namespace action
{

namespace builder
{

class Init_Move_GetResult_Response_result
{
public:
  explicit Init_Move_GetResult_Response_result(::agv_controller::action::Move_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::agv_controller::action::Move_GetResult_Response result(::agv_controller::action::Move_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_controller::action::Move_GetResult_Response msg_;
};

class Init_Move_GetResult_Response_status
{
public:
  Init_Move_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_GetResult_Response_result status(::agv_controller::action::Move_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Move_GetResult_Response_result(msg_);
  }

private:
  ::agv_controller::action::Move_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_controller::action::Move_GetResult_Response>()
{
  return agv_controller::action::builder::Init_Move_GetResult_Response_status();
}

}  // namespace agv_controller


namespace agv_controller
{

namespace action
{

namespace builder
{

class Init_Move_FeedbackMessage_feedback
{
public:
  explicit Init_Move_FeedbackMessage_feedback(::agv_controller::action::Move_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::agv_controller::action::Move_FeedbackMessage feedback(::agv_controller::action::Move_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::agv_controller::action::Move_FeedbackMessage msg_;
};

class Init_Move_FeedbackMessage_goal_id
{
public:
  Init_Move_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Move_FeedbackMessage_feedback goal_id(::agv_controller::action::Move_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Move_FeedbackMessage_feedback(msg_);
  }

private:
  ::agv_controller::action::Move_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::agv_controller::action::Move_FeedbackMessage>()
{
  return agv_controller::action::builder::Init_Move_FeedbackMessage_goal_id();
}

}  // namespace agv_controller

#endif  // AGV_CONTROLLER__ACTION__DETAIL__MOVE__BUILDER_HPP_
