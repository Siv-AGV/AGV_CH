// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from pgv100:msg/PGVScan.idl
// generated code does not contain a copyright notice
#include "pgv100/msg/detail/pgv_scan__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `direction`
#include "rosidl_runtime_c/string_functions.h"

bool
pgv100__msg__PGVScan__init(pgv100__msg__PGVScan * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    pgv100__msg__PGVScan__fini(msg);
    return false;
  }
  // x_position
  // y_position
  // angle
  // direction
  if (!rosidl_runtime_c__String__init(&msg->direction)) {
    pgv100__msg__PGVScan__fini(msg);
    return false;
  }
  // color_lane_count
  // no_color_lane
  // no_position
  // tag_detected
  return true;
}

void
pgv100__msg__PGVScan__fini(pgv100__msg__PGVScan * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // x_position
  // y_position
  // angle
  // direction
  rosidl_runtime_c__String__fini(&msg->direction);
  // color_lane_count
  // no_color_lane
  // no_position
  // tag_detected
}

bool
pgv100__msg__PGVScan__are_equal(const pgv100__msg__PGVScan * lhs, const pgv100__msg__PGVScan * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // x_position
  if (lhs->x_position != rhs->x_position) {
    return false;
  }
  // y_position
  if (lhs->y_position != rhs->y_position) {
    return false;
  }
  // angle
  if (lhs->angle != rhs->angle) {
    return false;
  }
  // direction
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->direction), &(rhs->direction)))
  {
    return false;
  }
  // color_lane_count
  if (lhs->color_lane_count != rhs->color_lane_count) {
    return false;
  }
  // no_color_lane
  if (lhs->no_color_lane != rhs->no_color_lane) {
    return false;
  }
  // no_position
  if (lhs->no_position != rhs->no_position) {
    return false;
  }
  // tag_detected
  if (lhs->tag_detected != rhs->tag_detected) {
    return false;
  }
  return true;
}

bool
pgv100__msg__PGVScan__copy(
  const pgv100__msg__PGVScan * input,
  pgv100__msg__PGVScan * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // x_position
  output->x_position = input->x_position;
  // y_position
  output->y_position = input->y_position;
  // angle
  output->angle = input->angle;
  // direction
  if (!rosidl_runtime_c__String__copy(
      &(input->direction), &(output->direction)))
  {
    return false;
  }
  // color_lane_count
  output->color_lane_count = input->color_lane_count;
  // no_color_lane
  output->no_color_lane = input->no_color_lane;
  // no_position
  output->no_position = input->no_position;
  // tag_detected
  output->tag_detected = input->tag_detected;
  return true;
}

pgv100__msg__PGVScan *
pgv100__msg__PGVScan__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pgv100__msg__PGVScan * msg = (pgv100__msg__PGVScan *)allocator.allocate(sizeof(pgv100__msg__PGVScan), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(pgv100__msg__PGVScan));
  bool success = pgv100__msg__PGVScan__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
pgv100__msg__PGVScan__destroy(pgv100__msg__PGVScan * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    pgv100__msg__PGVScan__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
pgv100__msg__PGVScan__Sequence__init(pgv100__msg__PGVScan__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pgv100__msg__PGVScan * data = NULL;

  if (size) {
    data = (pgv100__msg__PGVScan *)allocator.zero_allocate(size, sizeof(pgv100__msg__PGVScan), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = pgv100__msg__PGVScan__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        pgv100__msg__PGVScan__fini(&data[i - 1]);
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
pgv100__msg__PGVScan__Sequence__fini(pgv100__msg__PGVScan__Sequence * array)
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
      pgv100__msg__PGVScan__fini(&array->data[i]);
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

pgv100__msg__PGVScan__Sequence *
pgv100__msg__PGVScan__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pgv100__msg__PGVScan__Sequence * array = (pgv100__msg__PGVScan__Sequence *)allocator.allocate(sizeof(pgv100__msg__PGVScan__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = pgv100__msg__PGVScan__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
pgv100__msg__PGVScan__Sequence__destroy(pgv100__msg__PGVScan__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    pgv100__msg__PGVScan__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
pgv100__msg__PGVScan__Sequence__are_equal(const pgv100__msg__PGVScan__Sequence * lhs, const pgv100__msg__PGVScan__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!pgv100__msg__PGVScan__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
pgv100__msg__PGVScan__Sequence__copy(
  const pgv100__msg__PGVScan__Sequence * input,
  pgv100__msg__PGVScan__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(pgv100__msg__PGVScan);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    pgv100__msg__PGVScan * data =
      (pgv100__msg__PGVScan *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!pgv100__msg__PGVScan__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          pgv100__msg__PGVScan__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!pgv100__msg__PGVScan__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
