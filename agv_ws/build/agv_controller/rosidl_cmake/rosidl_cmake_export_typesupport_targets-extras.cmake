# generated from
# rosidl_cmake/cmake/template/rosidl_cmake_export_typesupport_targets.cmake.in

set(_exported_typesupport_targets
  "__rosidl_generator_c:agv_controller__rosidl_generator_c;__rosidl_typesupport_fastrtps_c:agv_controller__rosidl_typesupport_fastrtps_c;__rosidl_generator_cpp:agv_controller__rosidl_generator_cpp;__rosidl_typesupport_fastrtps_cpp:agv_controller__rosidl_typesupport_fastrtps_cpp;__rosidl_typesupport_introspection_c:agv_controller__rosidl_typesupport_introspection_c;__rosidl_typesupport_c:agv_controller__rosidl_typesupport_c;__rosidl_typesupport_introspection_cpp:agv_controller__rosidl_typesupport_introspection_cpp;__rosidl_typesupport_cpp:agv_controller__rosidl_typesupport_cpp;__rosidl_generator_py:agv_controller__rosidl_generator_py")

# populate agv_controller_TARGETS_<suffix>
if(NOT _exported_typesupport_targets STREQUAL "")
  # loop over typesupport targets
  foreach(_tuple ${_exported_typesupport_targets})
    string(REPLACE ":" ";" _tuple "${_tuple}")
    list(GET _tuple 0 _suffix)
    list(GET _tuple 1 _target)

    set(_target "agv_controller::${_target}")
    if(NOT TARGET "${_target}")
      # the exported target must exist
      message(WARNING "Package 'agv_controller' exports the typesupport target '${_target}' which doesn't exist")
    else()
      list(APPEND agv_controller_TARGETS${_suffix} "${_target}")
    endif()
  endforeach()
endif()
