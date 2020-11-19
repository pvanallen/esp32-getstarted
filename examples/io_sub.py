#
# example ESP8266 or ESP32 Huzzah mqtt subscribe with io.adafruit.com
# phil van allen
#
# thanks to https://github.com/MikeTeachman/micropython-adafruit-mqtt-esp8266/blob/master/mqtt-to-adafruit.py
# https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/example_sub.py
#

import network
import time
import machine
from umqtt.simple import MQTTClient

delay = 0.5
led_pin = machine.Pin(13, machine.Pin.OUT) # LED on the board

def sub_cb(topic, msg):
    # print(topic,msg)
    value = float(str(msg,'utf-8')) # convert subscribed value to a float
    print("subscribed value = {}".format(value))
    # turn on an LED if the value is greater than 2
    if value > 2:
      led_pin.value(1)
    else:
      led_pin.value(0)
#
# This code assumes the ESP32 is already connect to WiFi
#

#
# configuration from io.adafruit.com: My Key
#
ADAFRUIT_IO_USERNAME = "<enter your Adafruit Username here>"  # can be found by clicking on "MY KEY" when viewing your account on io.adafruit.com
ADAFRUIT_IO_KEY = "<enter your Adafruit IO Key here>"  # can be found by clicking on "MY KEY" when viewing your account on io.adafruit.com

# only one program with the same MqttClient Name can access the Adarfuit service at a time
myMqttClient = "phils_client1" # replace with your own client name unique to you and this code instance
adafruitFeed = ADAFRUIT_IO_USERNAME + "/feeds/test" # replace "test" with your feed name
adafruitIoUrl = "io.adafruit.com"

#
# connect ESP to Adafruit IO using MQTT
#
def connect_mqtt():
    c = MQTTClient(myMqttClient, adafruitIoUrl, 0, ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY, keepalive=10000)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(bytes(adafruitFeed,'utf-8'))
    return c

c = connect_mqtt()

start_time = time.time()
time_keeper = time.time()
print("Waiting for any changes in",adafruitFeed + "...")

while True:
    try:
        if time.time() - time_keeper > 5:
            print(time.time() - start_time,"secs elapsed")
            time_keeper = time.time()
        c.check_msg()
    except:
        # sometimes io.adafruit.com disconnects with an error
        print("error from io.adafruit - reconnecting...")
        # create a new connection
        c = connect_mqtt()
        pass

    time.sleep(delay)

c.disconnect()
