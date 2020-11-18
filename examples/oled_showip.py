import time
import machine
import network
import ssd1306 # https://github.com/micropython/micropython/tree/master/drivers/display

# set up I2C
i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))

# the ssd1306 module uses framebuf from MicroPyhon
# https://docs.micropython.org/en/latest/library/framebuf.html?highlight=framebuf
# for setting the "color" of elements in the display:
# 0 = black, 1 = white
# create the oled object with the 128x32 dimesions of the display at I2C address 0x3c
oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3c)

sta_if = network.WLAN(network.STA_IF)
ipaddress = sta_if.ifconfig()[0] # assumes device is already connected to WiFi

oled.fill(1) # wipe the display with white
oled.text('IP='+ipaddress, 0, 0,0) # put ip address on the screen at position 0,0, white
oled.show() # show what's been written to the display
