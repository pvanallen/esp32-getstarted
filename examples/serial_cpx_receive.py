# CircuitPython Demo - USB/Serial echo
# https://circuitpython.readthedocs.io/en/6.0.x/shared-bindings/busio/index.html?highlight=uart#busio.UART

import board
import busio
import time
from adafruit_circuitplayground import cp

uart = busio.UART(board.TX, board.RX, baudrate=9600,timeout=0.1)

while True:
    data = uart.readline(32)  # read up to 32 bytes

    if data is not None:

        # blink the LED if we got something
        cp.red_led = True
        time.sleep(0.05)
        cp.red_led = False

        data_string = None
        # convert the bytearray we received to a string & remove the line feed at the end
        data_string = ''.join([chr(b) for b in data])[:-1]

        try:
            data_float = float(data_string)
            print("got float:",data_float)
        except:
            if data_string.isdigit():
                data_float = int(data_string)
                print("got int:",data_float)
            else:
                print("got string:",data_string)
                data_float = None

        if data_float is not None: # work with a number
            # act on the data received
            if data_float > 100:
                cp.play_file("Wild_Eep.wav")
            elif data_float < 50:
                for x in range(0,10,1):
                    cp.pixels[x-1] = (0, 0, 255)
                    cp.pixels[x] = (255, 0, 0)
                    time.sleep(0.1)
            elif data_float >= 50 and data_float <= 100:
                for x in range(0,10,1):
                    cp.pixels[x] = (0, 0, 0)
                    time.sleep(0.1)

        if data_string is not None: # work with a string
            # act on the data received
            if data_string == "hello":
                cp.play_file("Wild_Eep.wav")
            elif data_string == "chase":
                for x in range(0,10,1):
                    cp.pixels[x-1] = (0, 0, 255)
                    cp.pixels[x] = (255, 0, 0)
                    time.sleep(0.1)
            elif data_string == "black":
                for x in range(0,10,1):
                    cp.pixels[x] = (0, 0, 0)
                    time.sleep(0.1)
