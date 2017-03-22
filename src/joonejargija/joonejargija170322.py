
"""
- k2ib m00da musta joont, kui satub valge peale siis 
"""

from ev3dev import ev3
from time import sleep

class Robot:
	def __init__(self):
		self.speed = 800
		self.motor_left = ev3.LargeMotor('outB')
		self.motor_right = ev3.LargeMotor('outC')
		self.color_sensor = ev3.ColorSensor('in2')
		self.color_sensor.mode = "COL-REFLECT" # 0-100

	def drive(self):
		self.motor_left.run_forever(speed_sp = self.speed)
		self.motor_right.run_forever(speed_sp = self.speed)

	def turn(self, direction):
		if direction == "right":
			self.motor_right.stop()
			self.motor_left.run_forever(speed_sp = self.speed)
		elif direction == "left":
			self.motor_left.stop()
			self.motor_right.run_forever(speed_sp = self.speed)

	def stop(self):
		self.motor_left.stop()
		self.motor_right.stop()


def main():
	try: 
		robot = Robot()

		robot.drive()
		time.sleep(4000)

		robot.turn("right")
		time.sleep(4000)

		robot.turn("left")
		time.sleep(4000)

		robot.stop()
	except KeyboardInterrupt:
		robot.stop()

if __name__ == "__main__":
	main()
