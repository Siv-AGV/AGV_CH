# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_canopen_kinco2_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED canopen_kinco2_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(canopen_kinco2_FOUND FALSE)
  elseif(NOT canopen_kinco2_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(canopen_kinco2_FOUND FALSE)
  endif()
  return()
endif()
set(_canopen_kinco2_CONFIG_INCLUDED TRUE)

# output package information
if(NOT canopen_kinco2_FIND_QUIETLY)
  message(STATUS "Found canopen_kinco2: 0.0.0 (${canopen_kinco2_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'canopen_kinco2' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${canopen_kinco2_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(canopen_kinco2_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${canopen_kinco2_DIR}/${_extra}")
endforeach()
