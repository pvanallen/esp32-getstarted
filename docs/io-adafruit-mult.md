## Using io.adafruit.com with multiple feeds/accounts

It is often useful to host multiple feeds on io.adafruit.com to track more than a single value. For example, your device may have sensors for light and touch. To work with multiple values, there are two strategies:

- Use multiple feeds within one account
- Use more than one io.adafruit account (may give you more bandwidth)

This code example shows how to use multiple feeds, though it could easily adapted to use multiple accounts by changing the username and key for the different accounts and/or feeds.

### Code Notes

Download code: [io_sub_mult.py](../examples/io_sub_mult.py)

This code assumes you are already connected to WiFi and can access the Internet.

#### Create a callback function to handle subscribed values

This function is called when any subscribed to values arrive from a feed. Note that it uses separate global variables for each feed subscription. This way, the most recent values are available at any time with having to wait for them to change and trigger a new receipt of a value.

**Be sure to change the global variables here and elsewhere to match your project feeds.**

```Python
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
```

#### Set your account/feed information

Sets up the information to connect with your io.adafruit.com account and feeds
```python
# create an Io object for each account and feed you are using
ADAFRUIT_IO_USERNAME = "account_username"
ADAFRUIT_IO_KEY = "account_key_password"
your_unique_id1 = 'client1' # replace with your own client name unique to you and this code instance
your_unique_id2 = 'client2' # replace with your own client name unique to you and this code instance
light_feed = 'light' # replace with your feed name
touch_feed = 'touch' # replace with your other feed name
```

#### Create Objects for each different account/feed

Creates the MQTT objects for connecting to io.adafruit.com - add more here with the appropriate values to have more than two feeds or accounts.

```python
# object format: Io(username, key, uniqueClientID, feedname)
phil_light = Io(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY, your_unique_id1, light_feed)
phil_touch = Io(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY, your_unique_id2, touch_feed)
#
# create named connections using the Io objects you created
#
io_light = connect_mqtt(phil_light)
io_touch = connect_mqtt(phil_touch)
```

#### Automatically receive the most recent feed values

You can optionally receive the most recent values from the feeds regardless of when they were last updated by using the [MQTT retain approach](https://io.adafruit.com/api/docs/mqtt.html?python#mqtt-retain).

```Python
# request that we get the last value from the feeds
# this sets up an MQTT "retain" https://io.adafruit.com/api/docs/mqtt.html?python#mqtt-retain
print("Requesting most recent values...")
io_light.publish(phil_light.feed + "/get", '\0')
io_touch.publish(phil_touch.feed + "/get", '\0')
```
#### Optionally publish values to the Feeds
This program subscribes to two feeds on one account. But by uncommenting these lines, you can also publish to the same two feeds. By default, it publishes random value. But you can change the code where the variables light_value and touch_value are set to use the appropriate code to get the current sensor values to be published.
```Python
      #
      # publish sensor values to feeds
      #
      # uncomment next 5 lines and replace the random code with code to get your sensor values
      light_value = 100 * random.random() # replace this random part with your sensor check code
      touch_value = 100 * random.random() # replace this random part with your sensor check code
      io_light.publish(phil_light.feed, str(light_value))
      io_touch.publish(phil_touch.feed, str(touch_value))
      print("Published values to light and touch: ",light_value,touch_value)
```

#### Subscribe to new values from the Feeds

Set up the subscription to each feed here with the named connections you created earlier

```Python
    # subscribe to feeds
    io_light.check_msg() # get values from the io_light account
    io_touch.check_msg() # get values from the io_touch account
```

#### Act on the feed values

Based on previous values, act on the global variables that retain the most recent subscribed values retrieved. In this case we are setting the board LED on or off depending on the values of the two feeds.

```Python
    # act on the cloud values
    if light_value > 10 and touch_value > 10:
        # turn ON the board LED
        led_pin.value(1)
    else:
        # turn OFF the board LED
        led_pin.value(0)
```

#### Deal with errors from the MQTT connection

If there's an error form MQTT, we close and recreate the connections.

```Python
  except:
      # sometimes io.adafruit.com disconnects with an error
      print("error from io.adafruit - reconnecting...")
      # create a new connection
      io_light.disconnect()
      io_touch.disconnect()
      io_light = connect_mqtt(phil_light)
      io_touch = connect_mqtt(phil_touch)
      pass
```
