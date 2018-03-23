## Using io.adafruit.com Cloud IoT Service

We can turn the ESP32 into a cloud connected device that can be controlled from anywhere in the world by using an IoT cloud service like [io.adafruit.com](https://io.adafruit.com/).

1.  Set up your account on io.adafruit.com and get your username and authorization key
2.  Enter this information into the code, along with your WiFi credentials
3.  Before you can run the below example programs, you must install an MQTT library on your device with the following commands. Be sure you have uploaded the boot.py file customized with your WiFi credentials. **You only need to do this once**.


```
>>> import boot
>>> boot.connect()
>>> import upip
>>> upip.install("micropython-umqtt.simple")
```

### [io_sub.py](../examples/io_sub.py)

Run this program and then go to your io.adafruit.com dashboard and add a data item to a feed called "test". Each time you add a new data item, it will show up on your device and turn an LED on (\>=4) or off (\<4). This because the program "subscribes" to that particular feed, and gets notified each time it changes.

### [io_pubsub.py](../examples/io_sub.py)

This code both publishes, and is subscribed to the cloud. Each time it sends a value to the cloud, it is immediately notified that a change happened for that feed. This simulates how you might set up two different devices, where one publishes, and the other subscribes to the same feed. This way, they can communicate to each other from any location.
