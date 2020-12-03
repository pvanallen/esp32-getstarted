# A simple example of sending data to another device
# Run the program, and type in the command value you want sent to the other device

from machine import UART
import time
from umqtt.simple import MQTTClient

uart = UART(1, 9600, tx=17, rx=16) # init with given baudrate that's that same as receiver
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

def sub_cb(topic, msg):
    # print(topic,msg)
    try:
        value = float(str(msg,'utf-8')) # convert subscribed value to a float
    except:
        value = msg.decode("utf-8")
    print("subscribed value = {}".format(value))
    uart.write(str(value) + "\n") # \n need for the reciver using readline()

#
# configuration from io.adafruit.com: My Key
#
ADAFRUIT_IO_USERNAME = "enter your Adafruit Username here"  # can be found at "My Account" at adafruit.com
ADAFRUIT_IO_KEY = "enter your Adafruit IO Key here"  # can be found by clicking on "MY KEY" when viewing your account on io.adafruit.com

# only one program with the same MqttClient Name can access the Adarfuit service at a time
myMqttClient = "your_unique_id" # replace with your own client name unique to you and this code instance
adafruitFeed = ADAFRUIT_IO_USERNAME + "/feeds/test" # replace "test" with your feed name

#
# connect ESP to Adafruit IO using MQTT
#
def connect_mqtt():
    c = MQTTClient(myMqttClient, "io.adafruit.com", 0, ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY, keepalive=10000)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(bytes(adafruitFeed,'utf-8'))

    return c

c = connect_mqtt()

print("Waiting for any changes in",adafruitFeed + "...")

while True:
    time.sleep(0.05)
    try:
        c.check_msg()
        pass
    except:
        # sometimes io.adafruit.com disconnects with an error
        print("error from io.adafruit - reconnecting...")
        # create a new connection
        c = connect_mqtt()
        pass
