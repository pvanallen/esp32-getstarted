from machine import Pin, PWM, ADC
import time

led = PWM(Pin(32), freq=5000) # create and configure

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)

delay = 0.02

while True:
  value = int(adc.read() * 0.25) # convert range 0-4095 to 0-1023
  led.duty(value)
  print(value)
  time.sleep(delay)
