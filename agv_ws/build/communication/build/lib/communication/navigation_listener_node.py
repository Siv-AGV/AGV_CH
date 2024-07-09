#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import socket
import json
from std_msgs.msg import String
from example_interfaces.srv import SetBool  # You might want to create a custom service type
import struct

PACK_FMT_STR = '!HHHHHLBB'

def pack_msg(req_id: int, api_code: int, msg=None):
        if msg is None:
            msg = {}
        msg_len = 0
        json_str = json.dumps(msg)
        if msg != {}:
            msg_len = len(json_str)
        raw_msg = struct.pack(PACK_FMT_STR, 0xCA00, 0x0001, 0x0000, req_id, api_code, msg_len, 0x00, 0x00)
        if msg != {}:
            raw_msg += bytearray(json_str, 'ascii')
        return raw_msg

class NavigationListenerNode(Node):
    def __init__(self):
        super().__init__('navigation_listener_node')
        self.declare_parameters(
            namespace='',
            parameters=[
                ('listen_host', 'localhost'), # Set IP to the machine's IP
                ('listen_port', 8000),
                ('listen_port2', 8100),
            ],
        )

        # Setup TCP server socket to listen for incoming connections
        self.listen_host = self.get_parameter('listen_host').get_parameter_value().string_value
        self.listen_port = self.get_parameter('listen_port').get_parameter_value().integer_value
        
        # self.listen_port2 = self.get_parameter('listen_port2').get_parameter_value().integer_value
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.listen_host, self.listen_port)) #insert kill all
        # self.server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server_socket2.bind((self.listen_host, self.listen_port2))

        self.get_logger().info('Connected')
        self.server_socket.listen(5)  # Listen for incoming connections with a backlog of 5
        # self.server_socket2.listen(5)

        self.client_socket = None
        self.client_address = None

        # ROS service to provide navigation data
        self.nav_service = self.create_service(SetBool, 'get_navigation_data', self.handle_navigation_request)

    def accept_connection(self):
        self.client_socket, self.client_address = self.server_socket.accept()
        self.get_logger().info(f'Accepted connection from {self.client_address}')

    

    def listen_for_navigation_data(self):
        while rclpy.ok():
            if self.client_socket is None:
                self.accept_connection()

            try:
                # Receive data from the client
                data = self.client_socket.recv(1024)  # Adjust buffer size as necessary
                # data = conn.recv(1024)
                header, json_data = data[:16], data[16:]
                header_data = struct.unpack(PACK_FMT_STR, header)
                req_id = header_data[3]
                api_code_id = header_data[4]
                json_data_len = header_data[5]
                data = json.loads(json_data) #this is python dictionary already.process from here to service or topic
                # print(f"Received api call from host, API code: {api_code_id}, JSON data: {json_data}")
                if data:
                    self.process_navigation_data(data)
                

                # need to reply to the RCS

                res_api_code = api_code_id + 10000
                # packed_data = pack_msg(req_id, res_api_code)
                self.client_socket.send(pack_msg(req_id, res_api_code))

            except Exception as e:
                self.get_logger().error(f'Failed to receive data: {e}')
                self.close_connection()

    def process_navigation_data(self, data):
        # Process and parse the incoming data
        try:
            # navigation_data = json.loads(data.decode('utf-8'))
            navigation_data = data
            # Log the received navigation data
            self.get_logger().info(f'Received navigation data: {navigation_data}')
            nav_task_list = navigation_data.get('nav_task_list', [])
            
            # Calculate the total number of tasks
            total_stations = len(nav_task_list)

            # Extract the path
            path = [int(task['from_id']) for task in nav_task_list] + [int(nav_task_list[-1]['to_id'])]

            self.get_logger().info(f'Total tasks: {total_stations}, Path: {path}')

        except json.JSONDecodeError as e:
            self.get_logger().error(f'Error decoding JSON data: {e}')

    def handle_navigation_request(self, request, response):
        # Assuming we store the last received navigation data
        response.success = True
        response.message = str(self.last_received_navigation_data)  # You need to implement storing this data
        return response

    def close_connection(self):
        if self.client_socket:
            self.client_socket.close()
            self.client_socket = None
            self.get_logger().info('Closed connection to client')

def main(args=None):
    rclpy.init(args=args)
    node = NavigationListenerNode()

    try:
        node.listen_for_navigation_data()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.close_connection()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
