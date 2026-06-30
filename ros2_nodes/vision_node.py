import rclpy
from rclpy.node import Node

from bs_msgs.msg import Detection
from bs_peripherals.vision.aggregator import DetectionAggregator
from bs_peripherals.utils.types import DetectionResult

class VisionNode(Node):
    def __init__(self):
        super().__init__('vision_node')

        self._aggregator = DetectionAggregator(history_size=10)

        self.subscription = self.create_subscription(
            Detection,
            '/vision/detections',
            self._on_detection,
            10
        )

        self.get_logger().info("vision node ready, listening on /vision/detections")    \
        

    def _on_detection(self, msg: Detection):
        detection_result = DetectionResult(
        class_id=msg.class_id,
        class_name=msg.class_name,
        confidence=msg.confidence,
        x_min=msg.x_min,
        y_min=msg.y_min,
        x_max=msg.x_max,
        y_max=msg.y_max,
        source_node=msg.source_node,
        stamp_ns=msg.stamp_ns
        )

        self._aggregator.add_detection(detection_result)
        self.get_logger().info(f"Received detection: {detection_result.class_name} with confidence {detection_result.confidence:.2f} from {detection_result.source_node}")  



def main(args=None):
    rclpy.init(args=args)
    node = VisionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()