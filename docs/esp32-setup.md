## Install software onto the ESP32 Huzzah board

**Download Micropython software binary for ESP32**

-   <https://micropython.org/download/esp32/>

Select the most recent stable ESP-IDF v3.x file, e.g. esp32-idf3-20200902-v1.13.bin

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
