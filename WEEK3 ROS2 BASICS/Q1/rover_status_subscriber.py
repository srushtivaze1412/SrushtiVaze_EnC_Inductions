#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import String
from std_msgs.msg import Bool


class RoverStatusSubscriber(Node):

    def __init__(self):
        super().__init__('rover_status_subscriber')

        self.battery = 0.0
        self.mode = ""
        self.emergency = False

        self.create_subscription(
            Float32,
            '/battery_level',
            self.battery_callback,
            10
        )

        self.create_subscription(
            String,
            '/rover_mode',
            self.mode_callback,
            10
        )

        self.create_subscription(
            Bool,
            '/emergency_stop',
            self.emergency_callback,
            10
        )

    def battery_callback(self, msg):
        self.battery = msg.data
        self.print_status()

    def mode_callback(self, msg):
        self.mode = msg.data
        self.print_status()

    def emergency_callback(self, msg):
        self.emergency = msg.data
        self.print_status()

    def print_status(self):
        self.get_logger().info(
            f"Battery: {self.battery} | "
            f"Mode: {self.mode} | "
            f"Emergency: {self.emergency}"
        )


def main(args=None):
    rclpy.init(args=args)

    node = RoverStatusSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
