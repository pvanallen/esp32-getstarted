## Coding Workflow

This page describes how do the repeating write and test code cycle (using a USB serial connection or a wireless WebREPL). And when your project is ready, how to deploy the project.

### Development - Serial Connection

-   Write code on computer
    -    Use your favorite text editor to create python code
    -    Save as .py file
    -    Sample code: [blink.py](../examples/blink.py)
-   Put a file/Get a file from the ESP32 device
    -    **Note**: You **must** exit the "screen" mode (Ctrl-A Ctrl-\\) to free up the USB port before you can use ampy to access device files
    - ```cd /directory/where/your/code/is```
    - ```ampy -p /dev/tty.SLAB_USBtoUART put blink.py```
    - ```ampy -p /dev/tty.SLAB_USBtoUART get blink.py```
-   Start the REPL
    - ```screen /dev/tty.SLAB\_USBtoUART 115200```
-   Run the python code with the device REPL using screen
    - ```import blink.py```
    - Test code
    - Use CTRL-C to exit code
    - Use CTRL-D to force a soft reboot
-   Exit "screen" and the REPL to allow sending new files to ESP32
    - ```Ctrl-A Ctrl-\```
-   Repeat

### Development - WebREPL

WebREPL enables you to access the device REPL through a browser, connecting through WiFi (using web sockets). You can access the ESP32 REPL and send/get files, all within the browser, and without a USB/Serial connection. For more info see the [WebREPL documentation](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html#webrepl-a-prompt-over-wifi).

-   The first time, you'll need to configure the ESP32 to allow WebREPL
    - After configuring WiFi in boot.py run ```import webrepl_setup```
    - Enter a passsword for accessing the REPL
    - Run ```import boot.py```
    - Connect to Wifi ```boot.connect()```
-   Get the IP address of your ESP32
    - Open a serial connection  ```screen /dev/tty.SLAB\_USBtoUART 115200```
    - Make sure you are connected to WiFi. If you've set up your boot.py correctly, when the device powers up you should be connected. Otherwise:
      -  ```import boot.py```
      - ```boot.connect()```
    - Get the IP address ```boot.showip()```
-   Open WebREPL in a browser window: http://micropython.org/webrepl
-   In the upper left, enter the IP address of your ESP32, while leaving the port number. It should look something like this: ws://10.0.1.171:8266/
-   Click on Connect, and you should be prompted for your Password
-   You then have access to the >>> REPL
-   You can also send or get files on the right hand side of the browser window

**NOTE**: In some cases ```import webrepl_setup``` does not work right and just returns without asking for a password, or there are other problems. Try the following if this is the case:
-   You may need to re upload your boot.py file and rerun import webrepl_setup
-   webrepl_setup attempts to add the following two lines at the end of your boot.py file and in some cases it doesn't work correctly. For example, you may see import webrepl added to the end of previous line in the file. So check that these two lines are in the boot.py file at the very end.
    - import webrepl
    - webrepl.start()
- webrepl_setup puts a new file on your device called webrepl_cfg.py, which contains your password. You may need to delete this file and try again.

### Deployment

When your code is fully tested and you want to deploy your project to run independently, do the following.

-   Name your code file ```main.py```. This will cause it to be run on power up/boot.
-   If your project requires network access, be sure your boot.py file is properly setup, and that the line with ```connect()``` is uncommented so that the device will connect to WiFi on boot.
-   Connect a LiPo battery to your device (remember that with the Adafruit HUZZAH32, you can recharge the battery by connect both the battery and power USB)
