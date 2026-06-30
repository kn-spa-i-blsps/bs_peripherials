import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from bs_peripherals.navigation.controller import NavigationController

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        self._controller = NavigationController()

        self._subscription = self.create_subscription(
            String,
            '/navigation/command',
            self._on_command,
            10
        )

        self.get_logger().info("navigation node ready, listening on /navigation/command")   



    def _on_command(self, msg: String) -> None:
        parts = msg.data.split(":")
        action = parts[0]

        value = float(parts[1]) if len(parts) > 1 else 0.0

        if action == "forward":
            self._controller.move_forward(value)
        elif action == "backward":
            self._controller.move_backward(value)
        elif action == "left":
            self._controller.move_left(value)
        elif action == "right":
            self._controller.move_right(value)
        elif action == "rotate":
            self._controller.rotate(value)
        elif action == "descend":
            self._controller.descend(value)
        elif action == "ascend":
            self._controller.ascend(value)
        elif action == "stop":
            self._controller.stop()
        else:
            self.get_logger().warn(f"Unknown command: {action}")



def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()