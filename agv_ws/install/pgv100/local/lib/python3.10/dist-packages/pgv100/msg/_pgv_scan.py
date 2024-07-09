# generated from rosidl_generator_py/resource/_idl.py.em
# with input from pgv100:msg/PGVScan.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_PGVScan(type):
    """Metaclass of message 'PGVScan'."""

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
            module = import_type_support('pgv100')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'pgv100.msg.PGVScan')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__pgv_scan
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__pgv_scan
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__pgv_scan
            cls._TYPE_SUPPORT = module.type_support_msg__msg__pgv_scan
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__pgv_scan

            from std_msgs.msg import Header
            if Header.__class__._TYPE_SUPPORT is None:
                Header.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class PGVScan(metaclass=Metaclass_PGVScan):
    """Message class 'PGVScan'."""

    __slots__ = [
        '_header',
        '_x_position',
        '_y_position',
        '_angle',
        '_direction',
        '_color_lane_count',
        '_no_color_lane',
        '_no_position',
        '_tag_detected',
    ]

    _fields_and_field_types = {
        'header': 'std_msgs/Header',
        'x_position': 'float',
        'y_position': 'float',
        'angle': 'float',
        'direction': 'string',
        'color_lane_count': 'uint8',
        'no_color_lane': 'uint8',
        'no_position': 'uint8',
        'tag_detected': 'uint8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        from std_msgs.msg import Header
        self.header = kwargs.get('header', Header())
        self.x_position = kwargs.get('x_position', float())
        self.y_position = kwargs.get('y_position', float())
        self.angle = kwargs.get('angle', float())
        self.direction = kwargs.get('direction', str())
        self.color_lane_count = kwargs.get('color_lane_count', int())
        self.no_color_lane = kwargs.get('no_color_lane', int())
        self.no_position = kwargs.get('no_position', int())
        self.tag_detected = kwargs.get('tag_detected', int())

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
        if self.header != other.header:
            return False
        if self.x_position != other.x_position:
            return False
        if self.y_position != other.y_position:
            return False
        if self.angle != other.angle:
            return False
        if self.direction != other.direction:
            return False
        if self.color_lane_count != other.color_lane_count:
            return False
        if self.no_color_lane != other.no_color_lane:
            return False
        if self.no_position != other.no_position:
            return False
        if self.tag_detected != other.tag_detected:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self):
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value):
        if __debug__:
            from std_msgs.msg import Header
            assert \
                isinstance(value, Header), \
                "The 'header' field must be a sub message of type 'Header'"
        self._header = value

    @builtins.property
    def x_position(self):
        """Message field 'x_position'."""
        return self._x_position

    @x_position.setter
    def x_position(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_position' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'x_position' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._x_position = value

    @builtins.property
    def y_position(self):
        """Message field 'y_position'."""
        return self._y_position

    @y_position.setter
    def y_position(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_position' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'y_position' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._y_position = value

    @builtins.property
    def angle(self):
        """Message field 'angle'."""
        return self._angle

    @angle.setter
    def angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._angle = value

    @builtins.property
    def direction(self):
        """Message field 'direction'."""
        return self._direction

    @direction.setter
    def direction(self, value):
        if __debug__:
            assert \
                isinstance(value, str), \
                "The 'direction' field must be of type 'str'"
        self._direction = value

    @builtins.property
    def color_lane_count(self):
        """Message field 'color_lane_count'."""
        return self._color_lane_count

    @color_lane_count.setter
    def color_lane_count(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'color_lane_count' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'color_lane_count' field must be an unsigned integer in [0, 255]"
        self._color_lane_count = value

    @builtins.property
    def no_color_lane(self):
        """Message field 'no_color_lane'."""
        return self._no_color_lane

    @no_color_lane.setter
    def no_color_lane(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'no_color_lane' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'no_color_lane' field must be an unsigned integer in [0, 255]"
        self._no_color_lane = value

    @builtins.property
    def no_position(self):
        """Message field 'no_position'."""
        return self._no_position

    @no_position.setter
    def no_position(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'no_position' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'no_position' field must be an unsigned integer in [0, 255]"
        self._no_position = value

    @builtins.property
    def tag_detected(self):
        """Message field 'tag_detected'."""
        return self._tag_detected

    @tag_detected.setter
    def tag_detected(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'tag_detected' field must be of type 'int'"
            assert value >= 0 and value < 256, \
                "The 'tag_detected' field must be an unsigned integer in [0, 255]"
        self._tag_detected = value
