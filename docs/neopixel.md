## WS2812 NeoPixel

The WS2812/NeoPixel (Adafruit's name) class of RGB (Red, Green, Blue) or RGBW (Red, Green, Blue, White) LEDs that can be used with microcontrollers and only need ground, power and a single wire to control as many LEDs as you want, where each LED is individually addressable.

The NeoPixels work well with the ESP32 with no additional software needed. And while the ESP32 has limited power available, it can support a 10-20 pixels okay, especially if you specify colors that are not full brightness. E.g. 128,0,0 for red instead of 255,0,0.

More info about NeoPixels:
* [Adafruit NeoPixel Überguide](https://learn.adafruit.com/adafruit-neopixel-uberguide)
* [Micropython Documentation](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/neopixel.html)

### How To

* **Define a NeoPixel chain** - You need to identify which GPIO pin is used to communicate with the NeoPixel chain, as well as define the number of pixels on the chain. Optionally, you can let the Micropython library know that you are using a 4 color NeoPixel - see the "bpp" parameter in the [Micropython docs](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/neopixel.html) for more info on this.

```np = neopixel.NeoPixel(machine.Pin(neopin), number_pixels)```

* **Set the colors of each pixel** - Using three or four parameters (3-Tuple or 4-Tuple), depending on the type of NeoPixel, set the color for specific pixels.

```np[0] = (255,0,0)```

* **Write the new values to the LEDs** - Only when you use the write() function do the LEDs actually change color with the new values you've set.

```np.write()```

### [neopixel_simple.py](../examples/neopixel_simple.py)

This is a basic example that sets the color of the first three pixels in a NeoPixel chain of 10.

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

### [neopixel_chase.py](../examples/neopixel_chase.py)

This example creates a chase effect where a red pixel seems to move from the beginning to the end of the chain. The code uses nested for loops to make the chase run four times.
