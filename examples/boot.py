yourWifiSSID = "<yourWifiSSID>"
yourWifiPassword = "<yourWifiPassword>"
def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(yourWifiSSID, yourWifiPassword)
        # while not sta_if.isconnected():
        #     pass
    print('network config:', sta_if.ifconfig())

def no_debug():
    import esp
    esp.osdebug(None) # this can be run from the REPL as well

def showip():
    import network
    sta_if = network.WLAN(network.STA_IF)
    print('network config:', sta_if.ifconfig())

# the next line can be uncommented if you want the ESP to connect
# to WiFi automatically when it boots. If you uncomment this, be sure
# you have tested it first with your network.
#
# connect()
#
# if you want to connect to the WiFi using the REPL, then type:
# >>> import boot
# >>> boot.connect()
#
