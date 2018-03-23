import time
import machine
from servo import Servo

servo_pin = machine.Pin(4)
my_servo = Servo(servo_pin)

my_servo.write_angle(0)
time.sleep(2)
my_servo.write_angle(180)
time.sleep(2)
my_servo.write_angle(90)
