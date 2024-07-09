// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from pgv100:msg/PGVScan.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "pgv100/msg/detail/pgv_scan__struct.h"
#include "pgv100/msg/detail/pgv_scan__functions.h"

#include "rosidl_runtime_c/string.h"
#include "rosidl_runtime_c/string_functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool pgv100__msg__pgv_scan__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[29];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("pgv100.msg._pgv_scan.PGVScan", full_classname_dest, 28) == 0);
  }
  pgv100__msg__PGVScan * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // x_position
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_position");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x_position = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y_position
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_position");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y_position = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->angle = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // direction
    PyObject * field = PyObject_GetAttrString(_pymsg, "direction");
    if (!field) {
      return false;
    }
    assert(PyUnicode_Check(field));
    PyObject * encoded_field = PyUnicode_AsUTF8String(field);
    if (!encoded_field) {
      Py_DECREF(field);
      return false;
    }
    rosidl_runtime_c__String__assign(&ros_message->direction, PyBytes_AS_STRING(encoded_field));
    Py_DECREF(encoded_field);
    Py_DECREF(field);
  }
  {  // color_lane_count
    PyObject * field = PyObject_GetAttrString(_pymsg, "color_lane_count");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->color_lane_count = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // no_color_lane
    PyObject * field = PyObject_GetAttrString(_pymsg, "no_color_lane");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->no_color_lane = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // no_position
    PyObject * field = PyObject_GetAttrString(_pymsg, "no_position");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->no_position = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // tag_detected
    PyObject * field = PyObject_GetAttrString(_pymsg, "tag_detected");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->tag_detected = (uint8_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * pgv100__msg__pgv_scan__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of PGVScan */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("pgv100.msg._pgv_scan");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "PGVScan");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  pgv100__msg__PGVScan * ros_message = (pgv100__msg__PGVScan *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x_position
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x_position);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_position", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_position
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y_position);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_position", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // direction
    PyObject * field = NULL;
    field = PyUnicode_DecodeUTF8(
      ros_message->direction.data,
      strlen(ros_message->direction.data),
      "replace");
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "direction", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // color_lane_count
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->color_lane_count);
    {
      int rc = PyObject_SetAttrString(_pymessage, "color_lane_count", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // no_color_lane
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->no_color_lane);
    {
      int rc = PyObject_SetAttrString(_pymessage, "no_color_lane", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // no_position
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->no_position);
    {
      int rc = PyObject_SetAttrString(_pymessage, "no_position", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // tag_detected
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->tag_detected);
    {
      int rc = PyObject_SetAttrString(_pymessage, "tag_detected", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
