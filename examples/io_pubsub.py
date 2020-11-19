#
# example ESP8266 or ESP32 Huzzah mqtt publish/subscribe with io.adafruit.com
# phil van allen
#
# for more info see: https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
# https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/example_sub.py
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

# configuration from io.adafruit.com
#
ADAFRUIT_IO_USERNAME = "<enter your Adafruit Username here>"  # can be found by clicking on "MY KEY" when viewing your account on io.adafruit.com
ADAFRUIT_IO_KEY = "<enter your Adafruit IO Key here>"  # can be found by clicking on "MY KEY" when viewing your account on io.adafruit.com
# only one program with the same MqttClient Name can access the Adarfuit service at a time
myMqttClient = "phils_client1" # replace with your own client name unique to you and this code instance
adafruitFeed = ADAFRUIT_IO_USERNAME + "/feeds/test" # replace "test" with your feed name
adafruitIoUrl = "io.adafruit.com"

#
# connect ESP to Adafruit IO using MQTT
def connect_mqtt():
    c = MQTTClient(myMqttClient, adafruitIoUrl, 0, ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY, keepalive=10000)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(bytes(adafruitFeed,'utf-8'))
    return c


#c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)
c = connect_mqtt()

for i in range(15):
  print(i)
  c.publish(adafruitFeed, str(i))
  time.sleep(2)
  c.check_msg()

c.disconnect()
