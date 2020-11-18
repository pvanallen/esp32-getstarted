import time
import machine
import ssd1306 # https://github.com/micropython/micropython/tree/master/drivers/display

# set up I2C
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))

# the ssd1306 module uses framebuf from MicroPyhon
# https://docs.micropython.org/en/latest/library/framebuf.html?highlight=framebuf
# for setting the "color" of elements in the display:
# 0 = black, 1 = white
# create the oled object with the 128x32 dimesions of the display at I2C address 0x3c
oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3c)

oled.fill(0) # wipe the display with black
oled.text('Hello World!', 0, 0) # put some text on the screen at position 0,0, default to white
oled.hline(0, 10, 128, 1) # create a horizontal line of width 128, starting at position 0,10, with color white
oled.show() # show what's been written to the display
