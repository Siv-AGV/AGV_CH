// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from pgv100:msg/PGVCommand.idl
// generated code does not contain a copyright notice
#include "pgv100/msg/detail/pgv_command__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
pgv100__msg__PGVCommand__init(pgv100__msg__PGVCommand * msg)
{
  if (!msg) {
    return false;
  }
  // command
  return true;
}

void
pgv100__msg__PGVCommand__fini(pgv100__msg__PGVCommand * msg)
{
  if (!msg) {
    return;
  }
  // command
}

bool
pgv100__msg__PGVCommand__are_equal(const pgv100__msg__PGVCommand * lhs, const pgv100__msg__PGVCommand * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // command
  if (lhs->command != rhs->command) {
    return false;
  }
  return true;
}

bool
pgv100__msg__PGVCommand__copy(
  const pgv100__msg__PGVCommand * input,
  pgv100__msg__PGVCommand * output)
{
  if (!input || !output) {
    return false;
  }
  // command
  output->command = input->command;
  return true;
}

pgv100__msg__PGVCommand *
pgv100__msg__PGVCommand__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pgv100__msg__PGVCommand * msg = (pgv100__msg__PGVCommand *)allocator.allocate(sizeof(pgv100__msg__PGVCommand), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(pgv100__msg__PGVCommand));
  bool success = pgv100__msg__PGVCommand__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
pgv100__msg__PGVCommand__destroy(pgv100__msg__PGVCommand * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    pgv100__msg__PGVCommand__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
pgv100__msg__PGVCommand__Sequence__init(pgv100__msg__PGVCommand__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pgv100__msg__PGVCommand * data = NULL;

  if (size) {
    data = (pgv100__msg__PGVCommand *)allocator.zero_allocate(size, sizeof(pgv100__msg__PGVCommand), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = pgv100__msg__PGVCommand__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        pgv100__msg__PGVCommand__fini(&data[i - 1]);
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
pgv100__msg__PGVCommand__Sequence__fini(pgv100__msg__PGVCommand__Sequence * array)
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
      pgv100__msg__PGVCommand__fini(&array->data[i]);
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

pgv100__msg__PGVCommand__Sequence *
pgv100__msg__PGVCommand__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  pgv100__msg__PGVCommand__Sequence * array = (pgv100__msg__PGVCommand__Sequence *)allocator.allocate(sizeof(pgv100__msg__PGVCommand__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = pgv100__msg__PGVCommand__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
pgv100__msg__PGVCommand__Sequence__destroy(pgv100__msg__PGVCommand__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    pgv100__msg__PGVCommand__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
pgv100__msg__PGVCommand__Sequence__are_equal(const pgv100__msg__PGVCommand__Sequence * lhs, const pgv100__msg__PGVCommand__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!pgv100__msg__PGVCommand__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
pgv100__msg__PGVCommand__Sequence__copy(
  const pgv100__msg__PGVCommand__Sequence * input,
  pgv100__msg__PGVCommand__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(pgv100__msg__PGVCommand);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    pgv100__msg__PGVCommand * data =
      (pgv100__msg__PGVCommand *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!pgv100__msg__PGVCommand__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          pgv100__msg__PGVCommand__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!pgv100__msg__PGVCommand__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
