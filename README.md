# wifi-analyzer
Scan and analyze WiFi access points with the ESP8266

## What you need / Dependencies:
- ESP8266 Microcontroller
- python3 with pip3
- adafruit-ampy: pip3 install adafruit-ampy
- esptool: pip3 install esptool
- micropython binary (search for the latest .bin on the internet)

## How to install
~~~
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 <esp8266-20171101-v1.9.3.bin>
~~~
Replace <esp8266-20171101-v1.9.3.bin> with the latest binary file.
~~~
ampy --port=/dev/ttyUSB0 put wifi_scanner.py main.py
~~~

## How to scan
To scan for networks and APs, hard reset your ESP8266 by removing the USB power supply and plugging it in again. The scan process will begin automatically.

## How to show logged SSIDs
Plug in your ESP via USB and run:
~~~
ampy --port=/dev/ttyUSB0 get ssid
~~~

## Disclaimer
The author is not responsible for problems caused by the use of this script. This is for educational purpose only.
