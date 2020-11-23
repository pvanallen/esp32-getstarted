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

last_value = -1

# set up the analog input
adc = machine.ADC(machine.Pin(39))
adc.atten(machine.ADC.ATTN_11DB)

# def sub_cb(topic, msg):
#     value = float(str(msg,'utf-8'))
#     print("subscribed value = {}".format(value))

#
# configuration from io.adafruit.com
#
ADAFRUIT_IO_USERNAME = "enter your Adafruit Username here"  # can be found at "My Account" at adafruit.com
ADAFRUIT_IO_KEY = "enter your Adafruit IO Key here"  # can be found by clicking on "MY KEY" when viewing your account on io.adafruit.com

# only one program with the same MqttClient Name can access the Adarfuit service at a time
myMqttClient = "your_unique_id" # replace with your own client name unique to you and this code
adafruitFeed = ADAFRUIT_IO_USERNAME + "/feeds/test" # replace "test" with your feed name
adafruitIoUrl = "io.adafruit.com"

#
# connect ESP to Adafruit IO using MQTT
#
def connect_mqtt():
    c = MQTTClient(myMqttClient, adafruitIoUrl, 0, ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY, keepalive=10000)
    c.connect()
    return c

c = connect_mqtt()

start_time = time.time()
while True:
  value = adc.read()

  if value != last_value or time.time() - start_time >= 20: # prevent sending duplicate values to keep traffic low
      try:
          c.publish(adafruitFeed, str(value))
          last_value = value
          print("published = " + str(value))
      except:
          # sometimes io.adafruit.com disconnects with an error
          print("error from io.adafruit - reconnecting...")
          # create a new connection
          c = connect_mqtt()
          pass
      start_time = time.time()
  # be careful about how frequently you send data to the cloud service
  # or they may limit your access
  time.sleep(5)

# c.disconnect()
