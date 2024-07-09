// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from pgv100:msg/PGVCommand.idl
// generated code does not contain a copyright notice

#ifndef PGV100__MSG__DETAIL__PGV_COMMAND__FUNCTIONS_H_
#define PGV100__MSG__DETAIL__PGV_COMMAND__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "pgv100/msg/rosidl_generator_c__visibility_control.h"

#include "pgv100/msg/detail/pgv_command__struct.h"

/// Initialize msg/PGVCommand message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * pgv100__msg__PGVCommand
 * )) before or use
 * pgv100__msg__PGVCommand__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
bool
pgv100__msg__PGVCommand__init(pgv100__msg__PGVCommand * msg);

/// Finalize msg/PGVCommand message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
void
pgv100__msg__PGVCommand__fini(pgv100__msg__PGVCommand * msg);

/// Create msg/PGVCommand message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * pgv100__msg__PGVCommand__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
pgv100__msg__PGVCommand *
pgv100__msg__PGVCommand__create();

/// Destroy msg/PGVCommand message.
/**
 * It calls
 * pgv100__msg__PGVCommand__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
void
pgv100__msg__PGVCommand__destroy(pgv100__msg__PGVCommand * msg);

/// Check for msg/PGVCommand message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
bool
pgv100__msg__PGVCommand__are_equal(const pgv100__msg__PGVCommand * lhs, const pgv100__msg__PGVCommand * rhs);

/// Copy a msg/PGVCommand message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
bool
pgv100__msg__PGVCommand__copy(
  const pgv100__msg__PGVCommand * input,
  pgv100__msg__PGVCommand * output);

/// Initialize array of msg/PGVCommand messages.
/**
 * It allocates the memory for the number of elements and calls
 * pgv100__msg__PGVCommand__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
bool
pgv100__msg__PGVCommand__Sequence__init(pgv100__msg__PGVCommand__Sequence * array, size_t size);

/// Finalize array of msg/PGVCommand messages.
/**
 * It calls
 * pgv100__msg__PGVCommand__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
void
pgv100__msg__PGVCommand__Sequence__fini(pgv100__msg__PGVCommand__Sequence * array);

/// Create array of msg/PGVCommand messages.
/**
 * It allocates the memory for the array and calls
 * pgv100__msg__PGVCommand__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
pgv100__msg__PGVCommand__Sequence *
pgv100__msg__PGVCommand__Sequence__create(size_t size);

/// Destroy array of msg/PGVCommand messages.
/**
 * It calls
 * pgv100__msg__PGVCommand__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
void
pgv100__msg__PGVCommand__Sequence__destroy(pgv100__msg__PGVCommand__Sequence * array);

/// Check for msg/PGVCommand message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
bool
pgv100__msg__PGVCommand__Sequence__are_equal(const pgv100__msg__PGVCommand__Sequence * lhs, const pgv100__msg__PGVCommand__Sequence * rhs);

/// Copy an array of msg/PGVCommand messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_pgv100
bool
pgv100__msg__PGVCommand__Sequence__copy(
  const pgv100__msg__PGVCommand__Sequence * input,
  pgv100__msg__PGVCommand__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // PGV100__MSG__DETAIL__PGV_COMMAND__FUNCTIONS_H_
