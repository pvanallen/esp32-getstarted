## Set up ESP Tools (Mac) -- [tutorial for Windows](https://lemariva.com/blog/2020/03/tutorial-getting-started-micropython-v20)

### Mac Computer Setup

There are a few steps required in order to work with the ESP32 and MicroPython.

**Xcode - Install the latest version of Xcode**

Xcode is Apple's software development environment, and while we won't be using it directly, it includes some tools that we will use. It is a very big download, so allow about 20 minutes to install it.

You can download it for free from the [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835?mt=12)
After installing Xcode, open the **Terminal** (in Applications>Utilities) program and run:

```xcode-select --install```

**Homebrew - Install this utility for managing development packages/systems**

Install this "package manager" that makes it easy to install other kinds of software on your computer. Homebrew is installed from your computer's Terminal program.

Go to the [Homebrew site](https://brew.sh) for installation instructions.

**Python3 and Pip3 - Install these essential tools**

Install Python3 & pip3:

```brew install python3```

**Install USB to Serial driver for Adafruit Huzzah32**

-   <https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers>
-   Use the .pkg for installation. If the standard driver does not work, try the "Legacy MacVCP Driver" folder (the newer one does not seem to work) - you may need to open system preferences to allow install to complete.
- Restart computer

**Install Command line tools to work with ESP32**

- Open a terminal window and install esptool and adafruit-ampy using the pip3 (i.e. for Python3) command. See [Homebrew](https://brew.sh/2017/07/31/homebrew-1.3.0/) for the easiest method for installing Python3 and pip3 (if you get a permissions error when using pip3, try prefixing it with "sudo ")
- ```pip3 install esptool```
- ```pip3 install adafruit-ampy```
