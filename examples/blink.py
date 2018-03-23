import machine
import time

#setup
pin = machine.Pin(13, machine.Pin.OUT) # LED on the board

#loop
while True:
  if pin.value() == 0:
    pin.value(1)
  else:
    pin.value(0)
  time.sleep(0.5)
