#
# example ESP8266 or ESP32 Huzzah mqtt publish with io.adafruit.com
# phil van allen
#
# thanks to https://github.com/MikeTeachman/micropython-adafruit-mqtt-esp8266/blob/master/mqtt-to-adafruit.py
#

import network
import time
import machine
from umqtt.simple import MQTTClient

adc = machine.ADC(machine.Pin(34))
adc.atten(machine.ADC.ATTN_11DB)

def sub_cb(topic, msg):
    value = float(str(msg,'utf-8'))
    print("subscribed value = {}".format(value))
    if value > 2:
      pin.value(1)
    else:
      pin.value(0)
#
# connect ESP to Adafruit IO using MQTT
#
myMqttClient = "<enter a unique client name here>"  # replace with your own client name
adafruitUsername = "<enter your Adafruit Username here>"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "<enter your Adafruit IO Key here>"  # can be found by clicking on "MY KEY" when viewing your account on io.adafruit.com
adafruitFeed = adafruitUsername + "/feeds/test" # replace "test" with your feed name
adafruitIoUrl = "io.adafruit.com"

c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)
c.set_callback(sub_cb)
c.connect()
c.subscribe(bytes(adafruitFeed,'utf-8'))

while True:
  value = adc.read()
  print("analog in read = ",value)

  c.publish(adafruitFeed, str(value))
  time.sleep(2)

c.disconnect()
