import machine
import time

adc = machine.ADC(machine.Pin(34))
adc.atten(machine.ADC.ATTN_11DB) # provides full range of 0-4095

led = machine.Pin(13, machine.Pin.OUT) # LED on the board

while True:
  value = adc.read() # reads in the range of 0-4095
  if value > 2048:
    led.value(1)
  else:
    led.value(0)
  print(value)
  time.sleep_ms(200)
