#
# example ESP32 multitasking
# phil van allen
#
# thanks to https://youtu.be/iyoS9aSiDWg
#
import time
import machine
import _thread as th

pin1 = machine.Pin(4)
pin2 = machine.Pin(13)
pwm1 = machine.PWM(pin1)
pwm2 = machine.PWM(pin2)
pwm1.freq(500)
pwm2.freq(500)

delay = 0.025

pwm1_running = True
pwm2_running = True

def fade(pwm, secs, run):
  steps = int(round(1024/(secs / delay / 2)))
  print(str(secs) + " " + str(steps) + " ")
  while run():
    for i in range(0,1024,steps):
      pwm.duty(i)
      time.sleep(delay)
    for i in range(1023, -1, (-1 * steps)):
      pwm.duty(i)
      time.sleep(delay)
  pwm.duty(0)

def pwm1_run():
  return pwm1_running

def pwm2_run():
  return pwm2_running

th.start_new_thread(fade, (pwm1,0.5,pwm1_run))
th.start_new_thread(fade, (pwm2,0.25,pwm2_run))

time.sleep(10)

pwm1_running = False
pwm2_running = False
