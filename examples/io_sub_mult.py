#
# example ESP32 Huzzah mqtt subscribe with io.adafruit.com
# this example shows using multiple feeds and saving values as they arrive to evaluate/compare later
# phil van allen
#
# for more info see: https://github.com/micropython/micropython-lib/tree/master/umqtt.simple
# https://github.com/micropython/micropython-lib/blob/master/umqtt.simple/example_sub.py
#

import time
import machine
import random
# Using the Micropython MQTT module
# TO INSTALL IT from the REPL (once your board is connected to WiFi)
# >>> import upip
# >>> upip.install("micropython-umqtt.simple")
from umqtt.simple import MQTTClient

delay = 0.2
led_pin = machine.Pin(13, machine.Pin.OUT) # LED on the board

# set up the global variables to retain cloud values for later processing
# see the function sub_cb() for where these are set
# also see the while True loop to see where they are evaluated
light_value = 0
touch_value = 0

# data structure for io.adafruit.com account + feed
class Io(object):
    def __init__(self, username, key, id, feed):
        self.username = username
        self.key = key
        self.id = id
        self.feed = username + "/feeds/" + feed

# callback function that runs when a value comes in from the cloud
def sub_cb(topic, msg):
    # put a global variable here for each feed you are monitoring
    global light_value, touch_value
    # print(topic,msg)
    feed = topic.decode("utf-8") # convert to string from bytes
    # handle floats and strings
    try:
        # float
        value = float(str(msg,'utf-8')) # convert subscribed value to a float
    except:
        # not a float so consider it a string
        value = msg.decode("utf-8")

    print("Received value from",feed,value)

    # check where the data came from and set the corresponding global variable
    # change these feeds to correspond to your io.adafruit username at the beginning
    if feed == "pvanallen/feeds/light":
        light_value = value
    if feed == "pvanallen/feeds/touch":
        touch_value = value
#
# This code assumes the ESP32 is already connect to WiFi
#

#
# set up the MQTT cloud connection
#
def connect_mqtt(io_account):
    c = MQTTClient(io_account.id, "io.adafruit.com", 0, io_account.username, io_account.key, keepalive=10000)
    c.set_callback(sub_cb)
    c.connect()
    adafruitFeed = io_account.feed
    c.subscribe(bytes(adafruitFeed,'utf-8'))
    return c

# configuration from io.adafruit.com
#
# create an Io object for each account and feed you are using
ADAFRUIT_IO_USERNAME = "pvanallen"
ADAFRUIT_IO_KEY = "ca67b97ac8adf9f9051f5333c72a53859af8ab07"
your_unique_id1 = 'philvanallen1' # replace with your own client name unique to you and this code instance
your_unique_id2 = 'philvanallen2' # replace with your own client name unique to you and this code instance
light_feed = 'light' # replace with your feed name
touch_feed = 'touch' # replace with your other feed name
# object format: Io(username, key, uniqueClientID, feedname)
phil_light = Io(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY, your_unique_id1, light_feed)
phil_touch = Io(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY, your_unique_id2, touch_feed)
#
# create named connections using the Io objects you created
#
io_light = connect_mqtt(phil_light)
io_touch = connect_mqtt(phil_touch)

start_time = time.time()
time_keeper = time.time()
print("Waiting for any changes in", phil_light.feed + "...")
print("Waiting for any changes in", phil_touch.feed + "...")

# request that we get the last value from the feeds
# this sets up an MQTT "retain" https://io.adafruit.com/api/docs/mqtt.html?python#mqtt-retain
print("Requesting most recent values...")
io_light.publish(phil_light.feed + "/get", '\0')
io_touch.publish(phil_touch.feed + "/get", '\0')

while True:
    try:
        if time.time() - time_keeper > 5:
            print(time.time() - start_time,"secs elapsed")
            time_keeper = time.time()
            print("Recent values for light",light_value,"touch",touch_value)
            #
            # publish sensor values to feeds
            #
            # uncomment next 5 lines and replace the random code with code to get your sensor values
            # light_value = 100 * random.random() # replace this random part with your sensor check code
            # touch_value = 100 * random.random() # replace this random part with your sensor check code
            # io_light.publish(phil_light.feed, str(light_value))
            # io_touch.publish(phil_touch.feed, str(touch_value))
            # print("Published values to light and touch: ",light_value,touch_value)

        # subscribe to feeds
        io_light.check_msg() # get values from the io_light account
        io_touch.check_msg() # get values from the io_touch account

        # act on the cloud values
        if light_value > 10 and touch_value > 10:
            # turn ON the board LED
            led_pin.value(1)
        else:
            # turn OFF the board LED
            led_pin.value(0)
    except:
        # sometimes io.adafruit.com disconnects with an error
        print("error from io.adafruit - reconnecting...")
        # create a new connection
        io_light.disconnect()
        io_touch.disconnect()
        io_light = connect_mqtt(phil_light)
        io_touch = connect_mqtt(phil_touch)
        pass


    time.sleep(delay)
