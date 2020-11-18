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

# analog to digital input
# https://docs.micropython.org/en/latest/esp32/quickref.html#adc-analog-to-digital-conversion
adc = machine.ADC(machine.Pin(34)) # A2
adc.atten(machine.ADC.ATTN_11DB) # set up range for max input voltage of 3.6V
adc.width(machine.ADC.WIDTH_12BIT) # values from 0-4095

while True:
  value = adc.read()
  oled.fill(0)
  oled.text('value = ' + str(value), 0, 0)
  value = int(value * 128/4096) # scale to the width of the display
  oled.hline(0,10, value, 1) # draw a line with a width of the ADC read
  oled.show()
  time.sleep_ms(200)
