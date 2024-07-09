#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Twist
from agv_msgs.srv import Move
import numpy as np
import math
from canopen_interfaces.srv import COWrite
from canopen_interfaces.msg import COData

class SimpleController(Node):
    def __init__(self):
        super().__init__("wheel_controller")
        self.declare_parameter("wheel_radius", 0.0875)
        self.declare_parameter("wheel_separation", 0.657)
        self.declare_parameter("max_acceleration", 0.1)
        self.declare_parameter("max_speed", 1.5) #robot linear speed

        self.wheel_radius = self.get_parameter("wheel_radius").get_parameter_value().double_value
        self.wheel_separation = self.get_parameter("wheel_separation").get_parameter_value().double_value
        self.max_acceleration = self.get_parameter("max_acceleration").get_parameter_value().double_value #robot linear acceleration
        self.max_speed = self.get_parameter("max_speed").get_parameter_value().double_value #robot max linear speed
        self.publisher_L = self.create_publisher(COData, '/motorL/tpdo', 10)
        self.publisher_R = self.create_publisher(COData, '/motorR/tpdo', 10)
        self.wheel_speed_pub = self.create_publisher(Float64MultiArray, 'wheel_speeds', 10)

        self.current_wheel_speed = np.array([0.0, 0.0])
        self.target_distance = 0.0
        self.target_angle = 0.0
        self.traveled_distance = 0.0
        self.traveled_angle = 0.0

        self.last_time = None
        self.moving = False

        self.speed_conversion = np.array([[self.wheel_radius / 2, self.wheel_radius / 2],
                                         [self.wheel_radius / self.wheel_separation, -self.wheel_radius / self.wheel_separation]])

        # self.wheel_cmd_pub = self.create_publisher(Float64MultiArray, "wheel_velocity_controller/commands", 10)
        self.service = self.create_service(Move, "wheel_control_service", self.command_callback)
        self.get_logger().info("Service is ready.")

    def command_callback(self, request, response):
        if not self.moving:  # Ensure it doesn't handle new requests if already moving
            msg = request.command
            self.target_distance = msg.linear.x
            self.target_angle = msg.angular.z

            self.traveled_distance = 0.0
            self.traveled_angle = 0.0

            self.last_time = self.get_clock().now()
            self.moving = True
            self.update_movement(response)

        return response

    def update_movement(self, response):
        if self.moving:
            current_time = self.get_clock().now()
            dt = (current_time - self.last_time).nanoseconds / 1e9
            self.last_time = current_time

            remaining_distance = self.target_distance - self.traveled_distance
            remaining_angle = self.target_angle - self.traveled_angle
            self.get_logger().info("Remaining Distance: " + str(remaining_distance))
            self.get_logger().info("Remaining Angle: " + str(remaining_angle))

            if abs(remaining_distance) <= 0.01 and abs(remaining_angle) <= 0.01:
                self.get_logger().info('Target reached. Stopping movement.')
                self.current_wheel_speed = np.array([0.0, 0.0])
                # self.publish_wheel_speeds()
                response.success = True
                self.moving = False
                return  # Stop the update cycle
                                    
            if abs(remaining_distance) > (0.2*abs(self.target_distance)):
            # Calculate the potential speed based on acceleration
                self.current_wheel_speed[0] += np.sign(remaining_distance) * self.max_acceleration * dt
                self.current_wheel_speed[1] += np.sign(remaining_angle) *(self.max_acceleration / self.wheel_separation) * dt

            # Adjust speeds based on remaining distance/angle to avoid overshoot
            # desired_linear_speed = np.sign(remaining_distance) * min(self.max_speed, abs(remaining_distance) / dt)
            # desired_angular_speed = np.sign(remaining_angle) * min(self.max_speed / self.wheel_separation, abs(remaining_angle) / dt)

                print ("potential speed: " + str(self.current_wheel_speed[0]))
            # print ("desired speed: " + str(desired_linear_speed))
            # linear_speed = np.sign(remaining_distance) * min(self.max_speed, abs(remaining_distance) / dt)
            # angular_speed = np.sign(remaining_angle) * min(self.max_speed / self.wheel_separation, abs(remaining_angle) / dt)
            # Apply ramp-up and slow-down logic
                linear_speed = np.sign(remaining_distance) * min(abs(self.current_wheel_speed[0]) , self.max_speed)
                angular_speed = np.sign(remaining_angle) * min(abs(self.current_wheel_speed[1]) , self.max_speed)

            if abs(remaining_distance) <= (0.5*abs(self.target_distance)):
                max_deceleration = 0.5
                self.current_wheel_speed[0] -= np.sign(self.current_wheel_speed[0]) *max_deceleration * dt
                self.current_wheel_speed[1] -= np.sign(self.current_wheel_speed[1]) *(max_deceleration / self.wheel_separation) * dt

                linear_speed = np.sign(self.current_wheel_speed[0]) * min(abs(self.current_wheel_speed[0]), self.max_speed)
                angular_speed = np.sign(self.current_wheel_speed[1]) * min(abs(self.current_wheel_speed[1]), self.max_speed)


                # deceleration_factor = 1.0 - (self.traveled_distance / self.target_distance)
                # linear_speed *= deceleration_factor
                # self.current_wheel_speed[0] -= np.sign(remaining_distance) * self.max_acceleration * dt
                # self.current_wheel_speed[1] -= np.sign(remaining_angle) *(self.max_acceleration / self.wheel_separation) * dt
                # linear_speed = np.sign(remaining_distance) * min(abs(self.current_wheel_speed[0]) , self.max_speed)
                # angular_speed = np.sign(remaining_angle) * min(abs(self.current_wheel_speed[1]) , self.max_speed)
                # linear_speed *= 0.8 #along the x-axis
                # linear_speed = np.sign(remaining_distance) * abs(linear_speed)  # Ensure the speed doesn't flip direction

            # if abs(remaining_angle) < 0.1:
            #     angular_speed *= abs(remaining_angle / 0.1) #around the z-axis
                # angular_speed = np.sign(remaining_angle) * abs(angular_speed)  # Ensure the speed doesn't flip direction

            # self odometry
            self.traveled_distance += linear_speed * dt
            self.traveled_angle += angular_speed * dt
   
            agv_speed = np.array([[linear_speed],
                                [angular_speed]])
            self.wheel_speed = np.matmul(np.linalg.inv(self.speed_conversion), agv_speed) 


            wheel_speed_msg = Float64MultiArray()
            wheel_speed_msg.data = [self.wheel_speed[1, 0],  self.wheel_speed[0, 0]]  ## [Left Wheel], [Right Wheel]
            if abs(self.wheel_speed[1, 0]) <= 0.001:
                self.wheel_speed[1, 0] = 0
            if abs(self.wheel_speed[0, 0]) <= 0.001:
                self.wheel_speed[0, 0] = 0
            # self.wheel_cmd_pub_.publish(wheel_speed_msg)
            self.current_wheel_speed_conv_L= int(abs((( self.wheel_speed[0]/(2*math.pi))*60*20 * 512 *10000)/1875))
            self.current_wheel_speed_conv_R= int(abs((( self.wheel_speed[1]/(2*math.pi))*60*20 * 512 *10000)/1875))
            # print ("DataCheck " + str(self.current_wheel_speed_conv))
            
            # self.current_wheel_speed_conv = round(self.current_wheel_speed_conv)

            print ("linear speed: " + str(linear_speed))
            print ("W_L: " + str( self.wheel_speed[1, 0]))
            print ("W_R: " + str( self.wheel_speed[0, 0]))
            print ("DataL: " + str(self.current_wheel_speed_conv_L))
            print ("DataR: " + str(self.current_wheel_speed_conv_R))


            # self.publish_wheel_speeds()
            self.publish_wheel_speed_L()
            self.publish_wheel_speed_R()


            if hasattr(self, 'timer') and self.timer:
                self.timer.cancel()

            # Continue updating if still moving
            timer_period = 0.06  # Adjust as necessary
            self.timer = self.create_timer(timer_period, lambda: self.update_movement(response))

            self.publish_wheel_speeds()
        else:
            self.current_wheel_speed_conv_L=0
            self.publish_wheel_speed_L()
            self.current_wheel_speed_conv_R=0
            self.publish_wheel_speed_R()
            # self.publish_wheel_speeds()
        
    def publish_wheel_speed_L(self):
        msg1 = COData()
        msg1.index = 0x60FF
        msg1.subindex = 0
        msg1.data = self.current_wheel_speed_conv_L
        self.publisher_L.publish(msg1)

    def publish_wheel_speed_R(self):
        msg2 = COData()
        msg2.index = 0x60FF
        msg2.subindex = 0
        msg2.data = self.current_wheel_speed_conv_R
        self.publisher_R.publish(msg2)

    def publish_wheel_speeds(self):

        print(f"Publishing wheel speeds: L={self.wheel_speed[0]}, R={self.wheel_speed[1]}")

    # Check for abnormal values
        if not (-1e5 < self.wheel_speed[0] < 1e5 and -1e5 < self.wheel_speed[1] < 1e5):
            # self.get_logger().error("Wheel speed out of expected range")
            return  # Skip publishing if values are out of a reasonable range

        wheel_speed_msg = Float64MultiArray()
        # wheel_speed_msg.layout.dim.append(MultiArrayDimension(label='speed', size=2, stride=2))
        wheel_speed_msg.data = [float(self.wheel_speed[0]), float(self.wheel_speed[1])]
        self.wheel_speed_pub.publish(wheel_speed_msg)



        # wheel_speed_msg = Float64MultiArray()
        # wheel_speed_msg.data = [[self.wheel_speed[0],  self.wheel_speed[1]]]
        # self.wheel_speed_pub.publish(wheel_speed_msg)

    

def main(args=None):
    rclpy.init()
    simple_controller = SimpleController()
    rclpy.spin(simple_controller)
    simple_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
