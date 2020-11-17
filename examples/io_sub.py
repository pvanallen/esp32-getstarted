#
# example ESP8266 or ESP32 Huzzah mqtt subscribe with io.adafruit.com
# phil van allen
#
# thanks to https://github.com/MikeTeachman/micropython-adafruit-mqtt-esp8266/blob/master/mqtt-to-adafruit.py
#

import network
import time
import machine
from umqtt.simple import MQTTClient

pin = machine.Pin(13, machine.Pin.OUT) # LED on the board

def sub_cb(topic, msg):
    value = float(str(msg,'utf-8'))
    print("subscribed value = {}".format(value))
    if value > 2:
      pin.value(1)
    else:
      pin.value(0)
#
# This code assumes the ESP32 is already connect to WiFi
#

# connect ESP to Adafruit IO using MQTT
#
myMqttClient = "<enter a unique client name here>"  # replace with your own client name
adafruitUsername = "<enter your Adafruit Username here>"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "<enter your Adafruit IO Key here>"  # can be found by clicking on "MY KEY" when viewing your account on io.adafruit.com
adafruitFeed = adafruitUsername + "/feeds/test" # replace "test" with your feed name
adafruitIoUrl = "io.adafruit.com"

myMqttClient = "pva"  # replace with your own client name
adafruitUsername = "pvanallen"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "ca67b97ac8adf9f9051f5333c72a53859af8ab07"  # can be found by clicking on "MY KEY" when viewing an Adafruit IO Feed
adafruitFeed = adafruitUsername + "/feeds/test" # replace "test" with your feed name
adafruitIoUrl = "io.adafruit.com"

c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)
c.set_callback(sub_cb)
c.connect()
c.subscribe(bytes(adafruitFeed,'utf-8'))

while True:
    c.check_msg()
    print("waiting...")
    # be careful how often you update, or adafruit may block you
    # the limit is 30 times maximum per minute
    time.sleep(3.0)

c.disconnect()
