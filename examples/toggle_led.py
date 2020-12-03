# Example code to show how a momentry button can be used to toggle an LED on and off
#
from machine import Pin
import time

led = Pin(32, Pin.OUT)
button = Pin(14, Pin.IN)

delay = 0.05

button_value = 0
button_value_last = 0
led_state = False

while True:
    button_value = button.value()

    # catch the transition from off to on (assumes a pullup resistor where button down is 1)
    if button_value == 0 and button_value_last == 1:
        led_state = not led_state

    button_value_last = button_value
    if led_state:
        led.value(1)
        print("on")
    else:
        led.value(0)
        print("off")

    time.sleep(delay)
