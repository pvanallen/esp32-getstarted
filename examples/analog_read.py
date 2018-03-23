import machine
import time

adc = machine.ADC(machine.Pin(34))
adc.atten(machine.ADC.ATTN_11DB)

while True:
  print(adc.read())
  time.sleep_ms(20)
