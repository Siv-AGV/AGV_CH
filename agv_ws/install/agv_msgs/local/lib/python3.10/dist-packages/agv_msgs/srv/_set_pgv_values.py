# generated from rosidl_generator_py/resource/_idl.py.em
# with input from agv_msgs:srv/SetPGVValues.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SetPGVValues_Request(type):
    """Metaclass of message 'SetPGVValues_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('agv_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'agv_msgs.srv.SetPGVValues_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_pgv_values__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_pgv_values__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_pgv_values__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_pgv_values__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_pgv_values__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetPGVValues_Request(metaclass=Metaclass_SetPGVValues_Request):
    """Message class 'SetPGVValues_Request'."""

    __slots__ = [
        '_x_offset',
        '_y_offset',
        '_z_offset',
    ]

    _fields_and_field_types = {
        'x_offset': 'double',
        'y_offset': 'double',
        'z_offset': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.x_offset = kwargs.get('x_offset', float())
        self.y_offset = kwargs.get('y_offset', float())
        self.z_offset = kwargs.get('z_offset', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.x_offset != other.x_offset:
            return False
        if self.y_offset != other.y_offset:
            return False
        if self.z_offset != other.z_offset:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def x_offset(self):
        """Message field 'x_offset'."""
        return self._x_offset

    @x_offset.setter
    def x_offset(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_offset' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'x_offset' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._x_offset = value

    @builtins.property
    def y_offset(self):
        """Message field 'y_offset'."""
        return self._y_offset

    @y_offset.setter
    def y_offset(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_offset' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'y_offset' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._y_offset = value

    @builtins.property
    def z_offset(self):
        """Message field 'z_offset'."""
        return self._z_offset

    @z_offset.setter
    def z_offset(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'z_offset' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'z_offset' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._z_offset = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_SetPGVValues_Response(type):
    """Metaclass of message 'SetPGVValues_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('agv_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'agv_msgs.srv.SetPGVValues_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__set_pgv_values__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__set_pgv_values__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__set_pgv_values__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__set_pgv_values__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__set_pgv_values__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SetPGVValues_Response(metaclass=Metaclass_SetPGVValues_Response):
    """Message class 'SetPGVValues_Response'."""

    __slots__ = [
        '_success',
        '_message',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
        'message': 'string',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())
        self.message = kwargs.get('message', str())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        if self.message != other.message:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value

    @builtins.property
    def message(self):
        """Message field 'message'."""
        return self._message

    @message.setter
    def message(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'message' field must be of type 'str'"
        self._message = value


class Metaclass_SetPGVValues(type):
    """Metaclass of service 'SetPGVValues'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('agv_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'agv_msgs.srv.SetPGVValues')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__set_pgv_values

            from agv_msgs.srv import _set_pgv_values
            if _set_pgv_values.Metaclass_SetPGVValues_Request._TYPE_SUPPORT is None:
                _set_pgv_values.Metaclass_SetPGVValues_Request.__import_type_support__()
            if _set_pgv_values.Metaclass_SetPGVValues_Response._TYPE_SUPPORT is None:
                _set_pgv_values.Metaclass_SetPGVValues_Response.__import_type_support__()


class SetPGVValues(metaclass=Metaclass_SetPGVValues):
    from agv_msgs.srv._set_pgv_values import SetPGVValues_Request as Request
    from agv_msgs.srv._set_pgv_values import SetPGVValues_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
