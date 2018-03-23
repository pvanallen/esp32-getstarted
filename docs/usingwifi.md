## Using WiFi

To make use of the ESP32 WiFi capabilities, you need a set of commands to configure the ESP to connect to your WiFi network with the correct SSID and Password.

Typically, this is done with a file called boot.py. This file is automatically run at each startup. For testing purposes, I don't recommend you have this file actually connect to the network, but rather make it easy to connect when you want to. Later, if you want to install your device permanently, you can set the boot.py file to automatically connect to the WiFi.

After putting boot.py (see below) on your device, use the REPL to do the following

    >>> import boot
    >>> boot.connect() # connects to WiFi
    >>> boot.showip() # tells you the IP address it got

### boot.py

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
