from machine import TouchPad, Pin
import time

# set up the touch Pin
t = TouchPad(Pin(14))
# set up the LED output for the built-in LED
led_pin = Pin(13, Pin.OUT) # LED on the board

delay = 0.2

while True:
    touched = t.read() # Returns a smaller number when touched
    print(touched)
    if touched < 110: # when touched, turn on the LED
      led_pin.value(1)
    else:
      led_pin.value(0)
    time.sleep(delay)
