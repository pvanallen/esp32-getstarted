#
# example ESP32 servo multitasking
# phil van allen
#
# thanks to servo library from https://bitbucket.org/thesheep/micropython-servo
#
import time
import machine
import _thread as th
from servo import Servo

pin1 = machine.Pin(15)
my_servo = Servo(pin1)
delay = 0.025

pwm1_running = True

def fade(secs, run):
  steps = int(round(180/(secs / delay / 2)))
  print(str(secs) + " " + str(steps) + " ")
  while run():
    for i in range(0,180,steps):
      my_servo.write_angle(i)
      time.sleep(delay)
    for i in range(180, -1, (-1 * steps)):
      my_servo.write_angle(i)
      time.sleep(delay)

def pwm1_run():
  return pwm1_running

th.start_new_thread(fade, (3,pwm1_run))

# do something else for 30 seconds
time.sleep(30)

pwm1_running = False
