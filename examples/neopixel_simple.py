#
# example ESP32 neopixel
# phil van allen
#
# see this page for more info:
# https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/neopixel.html
#
import machine
import neopixel
import time

neopin = 4
number_pixels = 10

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

np = neopixel.NeoPixel(machine.Pin(neopin), number_pixels)

np[0] = red
np[1] = green
np[2] = blue
np.write()
