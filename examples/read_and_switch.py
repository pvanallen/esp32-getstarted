import machine
import time

adc = machine.ADC(machine.Pin(34))
adc.atten(machine.ADC.ATTN_11DB)

led = machine.Pin(13, machine.Pin.OUT) # LED on the board

while True:
  if adc.read() > 2048:
    led.value(1)
  else:
    led.value(0)
  time.sleep_ms(20)
