import machine
import time

#setup
led = machine.Pin(13, machine.Pin.OUT) # LED on the board

#loop
while True:
  if led.value() == 0:
    led.value(1)
  else:
    led.value(0)
  time.sleep(0.5)
