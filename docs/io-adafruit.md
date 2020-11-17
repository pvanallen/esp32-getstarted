## Using io.adafruit.com Cloud IoT Service

We can turn the ESP32 into a cloud connected device that can be controlled from anywhere in the world by using an IoT cloud service like [io.adafruit.com](https://io.adafruit.com/).

1.  Set up your account on [io.adafruit.com](https://io.adafruit.com/)
1.  Go to Feeds -> Actions, and create a new Feed (data stream) with a single field (e.g. named "mydata")
1.  From the sidebar, select "View AIO Key" and get your username and key
1.  Enter this information into the code examples, (along with your WiFi credentials if needed - you may already be connecting to WiFi through your boot.py)
1.  Change the myMqttClient in the code to a unique name for each different client you run simultaneously. If you use the same name for simultaneous connections to io.adafruit.com, you will get errors.
1.  Before you can run the below example programs, you must install an MQTT library on your device. You use the upip command to install Python modules in Microphyhon, and this requires that WiFi be connected. So be sure you have uploaded the boot.py file customized with your WiFi credentials. **You only need to do this once**.
1. Run the following commands to connect to WiFi and install the mqtt module.

### Install MQTT library on your device
To do this, you MUST be connected to wifi

```
>>> import boot
>>> boot.connect()
>>> import upip
>>> upip.install("micropython-umqtt.simple")
```

### [io_sub.py](../examples/io_sub.py)

Run this program and then go to your io.adafruit.com dashboard and add a data item to a feed called "test". Each time you add a new data item, it will show up on your device and turn an LED on (\>2) or off (\<2). This is because this program "subscribes" to that particular feed, and gets notified each time it changes.

### [io_pub.py](../examples/io_pub.py)

Run this program to repeatedly send values from an analog input to the cloud. Then go to your io.adafruit.com dashboard and watch the values arrive in the feed called "test".

### [io_pubsub.py](../examples/io_pubsub.py)

This code both publishes, and is subscribed to the cloud. Each time it sends a value to the cloud, it is immediately notified that a change happened for that feed. This simulates how you might set up two different devices, where one publishes, and the other subscribes to the same feed. This way, they can communicate to each other from any location.
