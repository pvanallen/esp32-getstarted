# A simple example of sending data to another device
# Run the program, and type in the command value you want sent to the other device

from machine import UART

uart = UART(1, 9600, tx=17, rx=16) # init with given baudrate that's that same as receiver
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

while True:
    cmd = input("type command: ") # get the value to send from the user
    uart.write(str(cmd) + "\n") # \n need for the reciver using readline()
    print("sending ",cmd)
