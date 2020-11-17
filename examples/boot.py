# boot.py file
# set up for the Huzzah ESP32 from adafruit
#   Works with an OLED Display even if the library is missing or the board is not attached
#   Starts the webrepl once WiFi is connected
#   Uses an external file called secrets.py that contains wifi credentials
#    in this format:

# secrets = {
#     'ssid' : 'yourWifiSSID',
#     'password' : 'yourWifiPassword',
#     'timezone' : "America/Los_Angeles", # http://worldtimeapi.org/timezones
#     'github_token' : 'fawfj23rakjnfawiefa',
#     'hackaday_token' : 'h4xx0rs3kret',
#     }

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
