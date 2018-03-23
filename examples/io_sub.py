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
    if value > 4:
      pin.value(1)
    else:
      pin.value(0)
#
# connect the ESP to local wifi network
#
yourWifiSSID = "<yourWifiSSID>"
yourWifiPassword = "<yourWifiPassword>"
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  sta_if.active(True)
  sta_if.connect(yourWifiSSID, yourWifiPassword)
  while not sta_if.isconnected():
    pass
print("connected to WiFi")
#
# connect ESP to Adafruit IO using MQTT
#
myMqttClient = "<enter a unique client name here>"  # replace with your own client name
adafruitUsername = "<enter your Adafruit Username here>"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "<enter your Adafruit IO Key here>"  # can be found by clicking on "VIEW AIO KEYS" when viewing an Adafruit IO Feed
adafruitFeed = adafruitUsername + "/feeds/test" # replace "test" with your feed name
adafruitIoUrl = "io.adafruit.com"

c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)
c.set_callback(sub_cb)
c.connect()
c.subscribe(bytes(adafruitFeed,'utf-8'))

while True:
    c.check_msg()
    print("waiting...")
    time.sleep(0.5)

c.disconnect()
