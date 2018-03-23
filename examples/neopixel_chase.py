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

delay = 0.25

neopin = 4
number_pixels = 10

red = (255,0,0)
green = (0,255,0)

np = neopixel.NeoPixel(machine.Pin(neopin), number_pixels)

for n in range(4): # chase 4 times
  np[0] = red
  np.write()
  time.sleep(delay)

  for i in range(1,number_pixels): # increment each pixel
    np[i] = red
    np[i-1] = green
    np.write()
    time.sleep(delay)

  np[number_pixels-1] = green
  np.write()
