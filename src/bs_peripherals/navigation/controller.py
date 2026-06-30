import logging 


log = logging.getLogger(__name__)

class NavigationController:
    class NavigationController:
        def __init__(self):
            log.info("NavigationController initialized")

        def move_forward(self, distance_m: float) -> None:
            log.info(f"PLACEHOLDER: move forward {distance_m}m")

        def move_backward(self, distance_m: float) -> None:
            log.info(f"PLACEHOLDER: move backward {distance_m}m")

        def move_left(self, distance_m: float) -> None:
            log.info(f"PLACEHOLDER: move left {distance_m}m")

        def move_right(self, distance_m: float) -> None:
            log.info(f"PLACEHOLDER: move right {distance_m}m")

        def rotate(self, angle_deg: float) -> None:
            log.info(f"PLACEHOLDER: rotate {angle_deg} degrees")

        def descend(self, depth_m: float) -> None:
            log.info(f"PLACEHOLDER: descend {depth_m}m")

        def ascend(self, depth_m: float) -> None:
            log.info(f"PLACEHOLDER: ascend {depth_m}m")

        def stop(self) -> None:
            log.info("PLACEHOLDER: stop all thrusters")