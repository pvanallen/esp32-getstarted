## Using WiFi

To make use of the ESP32 WiFi capabilities, you need a set of commands to configure the ESP to connect to your WiFi network with the correct SSID and Password.

Typically, this is done with a file called boot.py. This file is automatically run at each startup (once boot.py has run, main.py will run next).

When first testing WiFi, I don't recommend you have this file actually connect to the network, but rather make it easy to connect when you want to. Later, if you want to install your device permanently, you can set the boot.py file to automatically connect to the WiFi by uncommenting the line at the bottom with "connect()"

After putting boot.py (see below) on your device, use the REPL to do the following

    >>> import boot
    >>> boot.connect() # connects to WiFi
    >>> boot.showip() # tells you the IP address it got

NOTE: The WebREPL is now implemented for ESP32. This enables you to access the REPL on the device through a web page (using web sockets). For more info see the [WebREPL documentation](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html#webrepl-a-prompt-over-wifi).

In short, after you've setup your boot.py file, you need to run:

    >>> import webrepl_setup

This will setup your webrepl password, and once connected to WiFi, you can go to:

http://micropython.org/webrepl

to access the REPL in your browser. It will also allow you to send and get files from the device. You'll need to know the IP address of the ESP32 to use WebREPL, which you can get with the below showip().

--------

### [boot_simple.py](../examples/boot_simple.py)
This example file is a simple version that sets up WiFi on boot. It depends on an external file
called [secrets.py](../examples/secrets.py). You'll need to put your own ssid and password in the appropriate fields.

    yourWifiSSID = ""
    yourWifiPassword = ""
    def connect():
        import network
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(yourWifiSSID, yourWifiPassword)
            # while the below while loop is part of the standard recommended approach,
            # I found it could hang the device if run with connect() on boot
            # while not sta_if.isconnected():
            #     pass
        print('network config:', sta_if.ifconfig())

    def showip():
        import network
        sta_if = network.WLAN(network.STA_IF)
        print('network config:', sta_if.ifconfig())

    # the connect() line can be uncommented if you want the ESP to connect
    # to WiFi automatically when it boots. If you uncomment this, be sure
    # you have tested it first with your network.
    #
    # connect()

### [boot.py](../examples/boot.py)
This example file works with an OLED Feather board that's connected to the ESP32. Get the necessary driver module (ssd1306.py) for the SSD1306 OLED from [here](https://github.com/micropython/micropython/tree/master/drivers/display), and install it on your ESP32 board.

    import webrepl
    import time
    import machine
    try:
        import ssd1306
        display_module = True
    except ImportError:
        print("ssd1306 OLED module not available")
        display_module = False

    wifi_timelimit = 5.0

    try:
        from secrets import secrets
        yourWifiSSID = secrets["ssid"]
        yourWifiPassword = secrets["password"]
    except ImportError:
        print("WiFi secrets are kept in secrets.py, please add them there!")
        raise

    i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))

    def connect():
        import network
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(yourWifiSSID, yourWifiPassword)
            print("connecting to " + yourWifiSSID + "...")

            start = time.time()
            while not sta_if.isconnected():
                if time.time() - start > wifi_timelimit:
                    print(" ")
                    print("**** TIMEOUT: too long a wait for connecting to WiFi - check ssid and password")
                    print(" ")
                    break
                pass
            ipaddress = sta_if.ifconfig()[0]
            print("connected to " + yourWifiSSID + ' with IP address:' , ipaddress)

            webrepl.start()
            if display_module:
                try:
                    oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3c)
                    display_connected = True
                    print("OLED display connected...")
                except OSError as err:
                    display_connected = False
                    print("Error connecting to OLED Display")
                    print("OLED: " + err)
                    if err == "[Errno 110] ETIMEDOUT":
                        print("OLED display NOT connected...")

                if display_connected:
                    oled.fill(0)
                    oled.text('Hello World!', 0, 0)
                    oled.text('IP=' + ipaddress, 0, 10)
                    oled.show()
            else:
                print("OLED display NOT setup because ssd1306.py module is not availabe...")

    def no_debug():
        import esp
        esp.osdebug(None) # this can be run from the REPL as well

    def showip():
        import network
        sta_if = network.WLAN(network.STA_IF)
        print('network config:', sta_if.ifconfig())

    # the connect() line can be uncommented if you want the ESP32 to connect
    # to WiFi automatically when it boots. If you uncomment this, be sure
    # you have tested it first with your network.
    #
    # connect()
    #
    # if you want to connect to the WiFi using the REPL, type:
    # >>> import boot
    # >>> boot.connect()
