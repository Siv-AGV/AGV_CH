// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from agv_msgs:srv/SetPGVValues.idl
// generated code does not contain a copyright notice
#include "agv_msgs/srv/detail/set_pgv_values__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
agv_msgs__srv__SetPGVValues_Request__init(agv_msgs__srv__SetPGVValues_Request * msg)
{
  if (!msg) {
    return false;
  }
  // x_offset
  // y_offset
  // z_offset
  return true;
}

void
agv_msgs__srv__SetPGVValues_Request__fini(agv_msgs__srv__SetPGVValues_Request * msg)
{
  if (!msg) {
    return;
  }
  // x_offset
  // y_offset
  // z_offset
}

bool
agv_msgs__srv__SetPGVValues_Request__are_equal(const agv_msgs__srv__SetPGVValues_Request * lhs, const agv_msgs__srv__SetPGVValues_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // x_offset
  if (lhs->x_offset != rhs->x_offset) {
    return false;
  }
  // y_offset
  if (lhs->y_offset != rhs->y_offset) {
    return false;
  }
  // z_offset
  if (lhs->z_offset != rhs->z_offset) {
    return false;
  }
  return true;
}

bool
agv_msgs__srv__SetPGVValues_Request__copy(
  const agv_msgs__srv__SetPGVValues_Request * input,
  agv_msgs__srv__SetPGVValues_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // x_offset
  output->x_offset = input->x_offset;
  // y_offset
  output->y_offset = input->y_offset;
  // z_offset
  output->z_offset = input->z_offset;
  return true;
}

agv_msgs__srv__SetPGVValues_Request *
agv_msgs__srv__SetPGVValues_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  agv_msgs__srv__SetPGVValues_Request * msg = (agv_msgs__srv__SetPGVValues_Request *)allocator.allocate(sizeof(agv_msgs__srv__SetPGVValues_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(agv_msgs__srv__SetPGVValues_Request));
  bool success = agv_msgs__srv__SetPGVValues_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
agv_msgs__srv__SetPGVValues_Request__destroy(agv_msgs__srv__SetPGVValues_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    agv_msgs__srv__SetPGVValues_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
agv_msgs__srv__SetPGVValues_Request__Sequence__init(agv_msgs__srv__SetPGVValues_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  agv_msgs__srv__SetPGVValues_Request * data = NULL;

  if (size) {
    data = (agv_msgs__srv__SetPGVValues_Request *)allocator.zero_allocate(size, sizeof(agv_msgs__srv__SetPGVValues_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = agv_msgs__srv__SetPGVValues_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        agv_msgs__srv__SetPGVValues_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
agv_msgs__srv__SetPGVValues_Request__Sequence__fini(agv_msgs__srv__SetPGVValues_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      agv_msgs__srv__SetPGVValues_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

agv_msgs__srv__SetPGVValues_Request__Sequence *
agv_msgs__srv__SetPGVValues_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  agv_msgs__srv__SetPGVValues_Request__Sequence * array = (agv_msgs__srv__SetPGVValues_Request__Sequence *)allocator.allocate(sizeof(agv_msgs__srv__SetPGVValues_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = agv_msgs__srv__SetPGVValues_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
agv_msgs__srv__SetPGVValues_Request__Sequence__destroy(agv_msgs__srv__SetPGVValues_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    agv_msgs__srv__SetPGVValues_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
agv_msgs__srv__SetPGVValues_Request__Sequence__are_equal(const agv_msgs__srv__SetPGVValues_Request__Sequence * lhs, const agv_msgs__srv__SetPGVValues_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!agv_msgs__srv__SetPGVValues_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
agv_msgs__srv__SetPGVValues_Request__Sequence__copy(
  const agv_msgs__srv__SetPGVValues_Request__Sequence * input,
  agv_msgs__srv__SetPGVValues_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(agv_msgs__srv__SetPGVValues_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    agv_msgs__srv__SetPGVValues_Request * data =
      (agv_msgs__srv__SetPGVValues_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!agv_msgs__srv__SetPGVValues_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          agv_msgs__srv__SetPGVValues_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!agv_msgs__srv__SetPGVValues_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `message`
#include "rosidl_runtime_c/string_functions.h"

bool
agv_msgs__srv__SetPGVValues_Response__init(agv_msgs__srv__SetPGVValues_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  // message
  if (!rosidl_runtime_c__String__init(&msg->message)) {
    agv_msgs__srv__SetPGVValues_Response__fini(msg);
    return false;
  }
  return true;
}

void
agv_msgs__srv__SetPGVValues_Response__fini(agv_msgs__srv__SetPGVValues_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
  // message
  rosidl_runtime_c__String__fini(&msg->message);
}

bool
agv_msgs__srv__SetPGVValues_Response__are_equal(const agv_msgs__srv__SetPGVValues_Response * lhs, const agv_msgs__srv__SetPGVValues_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // message
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->message), &(rhs->message)))
  {
    return false;
  }
  return true;
}

bool
agv_msgs__srv__SetPGVValues_Response__copy(
  const agv_msgs__srv__SetPGVValues_Response * input,
  agv_msgs__srv__SetPGVValues_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  // message
  if (!rosidl_runtime_c__String__copy(
      &(input->message), &(output->message)))
  {
    return false;
  }
  return true;
}

agv_msgs__srv__SetPGVValues_Response *
agv_msgs__srv__SetPGVValues_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  agv_msgs__srv__SetPGVValues_Response * msg = (agv_msgs__srv__SetPGVValues_Response *)allocator.allocate(sizeof(agv_msgs__srv__SetPGVValues_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(agv_msgs__srv__SetPGVValues_Response));
  bool success = agv_msgs__srv__SetPGVValues_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
agv_msgs__srv__SetPGVValues_Response__destroy(agv_msgs__srv__SetPGVValues_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    agv_msgs__srv__SetPGVValues_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
agv_msgs__srv__SetPGVValues_Response__Sequence__init(agv_msgs__srv__SetPGVValues_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  agv_msgs__srv__SetPGVValues_Response * data = NULL;

  if (size) {
    data = (agv_msgs__srv__SetPGVValues_Response *)allocator.zero_allocate(size, sizeof(agv_msgs__srv__SetPGVValues_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = agv_msgs__srv__SetPGVValues_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        agv_msgs__srv__SetPGVValues_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
agv_msgs__srv__SetPGVValues_Response__Sequence__fini(agv_msgs__srv__SetPGVValues_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      agv_msgs__srv__SetPGVValues_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

agv_msgs__srv__SetPGVValues_Response__Sequence *
agv_msgs__srv__SetPGVValues_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  agv_msgs__srv__SetPGVValues_Response__Sequence * array = (agv_msgs__srv__SetPGVValues_Response__Sequence *)allocator.allocate(sizeof(agv_msgs__srv__SetPGVValues_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = agv_msgs__srv__SetPGVValues_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
agv_msgs__srv__SetPGVValues_Response__Sequence__destroy(agv_msgs__srv__SetPGVValues_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    agv_msgs__srv__SetPGVValues_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
agv_msgs__srv__SetPGVValues_Response__Sequence__are_equal(const agv_msgs__srv__SetPGVValues_Response__Sequence * lhs, const agv_msgs__srv__SetPGVValues_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!agv_msgs__srv__SetPGVValues_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
agv_msgs__srv__SetPGVValues_Response__Sequence__copy(
  const agv_msgs__srv__SetPGVValues_Response__Sequence * input,
  agv_msgs__srv__SetPGVValues_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(agv_msgs__srv__SetPGVValues_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    agv_msgs__srv__SetPGVValues_Response * data =
      (agv_msgs__srv__SetPGVValues_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!agv_msgs__srv__SetPGVValues_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          agv_msgs__srv__SetPGVValues_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!agv_msgs__srv__SetPGVValues_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
