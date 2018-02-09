# wifi-analyzer
Scan and analyze WiFi access points with the ESP8266

## What you need / Dependencies:
- ESP8266 Microcontroller
- python3 with pip3
- adafruit-ampy: pip3 install adafruit-ampy
- esptool: pip3 install esptool
- micropython binary

## How to install
~~~
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 esp8266-20171101-v1.9.3.bin

~~~
