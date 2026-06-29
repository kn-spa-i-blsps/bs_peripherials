from bs_peripherals.servo.driver import PCA9685Driver
from bs_peripherals.servo.payload import PayloadController
from bs_peripherals.utils.types import PayloadAction

driver = PCA9685Driver()
controller = PayloadController(driver)

controller.execute(PayloadAction.DROP_BALL_1)