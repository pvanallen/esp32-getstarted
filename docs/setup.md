## Set up computer Mac for now -- ([tutorial for Windows](https://lemariva.com/blog/2017/10/micropython-getting-started))

**Install USB to Serial driver for Adafruit Huzzah32**

-   <https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers>
-   Use the .pkg for installation. If the standard driver does not work, try the "Legacy MacVCP Driver" folder (the newer one does not seem to work) - you may need to open system preferences to allow install to complete.
- Restart computer

**Install Command line tools to work with ESP32**

- Open a terminal window and install esptool and adafruit-ampy using the pip3 (i.e. for Python3) command. See [Homebrew](https://brew.sh/2017/07/31/homebrew-1.3.0/) for the easiest method for installing Python3 and pip3 (if you get a permissions error when using pip3, try prefixing it with "sudo ")
- ```pip3 install esptool```
- ```pip3 install adafruit-ampy```

**Download Micropython software binary for ESP32**

-   <https://micropython.org/download/esp32/>

Select the most recent stable file, e.g. esp32-idf3-20200902-v1.13.bin

## Set up ESP32    

-   Connect device by USB
-   Check the name of serial port, looking for one with "SLAB" in it:
    - ```ls /dev/tty*```
-   Erase the device (must be done the fist time micropython is installed, or if device becomes stuck due to other problems)
    - ```esptool.py --chip esp32 -p /dev/tty.SLAB_USBtoUART erase_flash```
-   Flash the micropython software
    - ```esptool.py --chip esp32 -p /dev/tty.SLAB_USBtoUART write_flash -z 0x1000 nameOfMicropythonBinary.bin```
-   Power off/on device after binary finishes installing, then reconnect to computer.
-   Try out the Python REPL on the device by opening a serial connection "terminal" to the device.
    - ```screen /dev/tty.SLAB_USBtoUART 115200```
    - hit return to see ">>> " prompt
    - ```help()```
    - ```print("hello")```
-   List files
    - ```import os```
    - ```os.listdir()```
-   Ctrl-A Ctrl-\\ to disconnect from device and get out of screen mode
-   See files on the device disk from computer command line
    - ```ampy -p /dev/tty.SLAB_USBtoUART ls```
