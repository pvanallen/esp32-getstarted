#
# example ESP8266 or ESP32 Huzzah mqtt publish with io.adafruit.com
# phil van allen
#
# for more info see: https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
#

import network
import time
import machine
from umqtt.simple import MQTTClient

last_value = -1

# set up the analog input
adc = machine.ADC(machine.Pin(39))
adc.atten(machine.ADC.ATTN_11DB)

def sub_cb(topic, msg):
    value = float(str(msg,'utf-8'))
    print("subscribed value = {}".format(value))
#
# configuration from io.adafruit.com
#
ADAFRUIT_IO_USERNAME = "<enter your Adafruit Username here>"  # can be found at "My Account" at adafruit.com
ADAFRUIT_IO_KEY = "<enter your Adafruit IO Key here>"  # can be found by clicking on "MY KEY" when viewing your account on io.adafruit.com

# only one program with the same MqttClient Name can access the Adarfuit service at a time
myMqttClient = "pva" # replace with your own client name unique to you and this code
adafruitFeed = ADAFRUIT_IO_USERNAME + "/feeds/test" # replace "test" with your feed name
adafruitIoUrl = "io.adafruit.com"

#
# connect ESP to Adafruit IO using MQTT
#
c = MQTTClient(myMqttClient, adafruitIoUrl, 0, ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
c.set_callback(sub_cb)
c.connect()
c.subscribe(bytes(adafruitFeed,'utf-8'))

while True:
  value = adc.read()
  print("analog read = ",value)

  if value != last_value: # prevent sending duplicate values to keep traffic low
      c.publish(adafruitFeed, str(value))
      last_value = value
  # be careful about how frequently you send data to the cloud service
  # or they may limit your access
  time.sleep(2)

c.disconnect()
