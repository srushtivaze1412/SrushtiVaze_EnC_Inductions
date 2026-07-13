#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from kratos_srushti_msgs.msg import RoverStatus


class RoverStatusPublisher(Node):

    def __init__(self):
        super().__init__('rover_status_msg_publisher')

        self.publisher = self.create_publisher(
            RoverStatus,
            '/rover_status',
            10
        )

        self.timer = self.create_timer(0.5, self.publish_status)

    def publish_status(self):

        msg = RoverStatus()

        msg.battery_percentage = 95.0
        msg.velocity = 2.5
        msg.emergency_stop = False
        msg.mode = "AUTONOMOUS"

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Battery={msg.battery_percentage}, '
            f'Velocity={msg.velocity}, '
            f'Emergency={msg.emergency_stop}, '
            f'Mode={msg.mode}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = RoverStatusPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
