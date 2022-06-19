## RaspberryPi Working with DHT22 Temperature and Umidity sensor

This project is a guide how to connect and read data from DHT22 sensor using a Raspberry Pi and Python code.

Lets start  🚀


### 1. Connect the sensor
The DHT22 sensor has 4 pins to be connect. The connection schema was presented in the image:

![Captura de Tela 2022-06-18 às 23 23 10](https://user-images.githubusercontent.com/13997912/174463222-022467fc-83a2-4794-b495-b583f6c92ae3.png)

On Raspberry Pi, the sensor will be connected on Pin1 (3.3v), Pin 6 (GND) and GPIO 23 (Pin 16) to send data from sensor to Raspberry Pi.


### 2. Install Adafruit Lib
To read data from DHT22 sensor, we need to use Adafruit DHT Lib, available on:
https://github.com/adafruit/Adafruit_Python_DHT.git

Clone Adafruit Lib to you project:

`git clone https://github.com/adafruit/Adafruit_Python_DHT.git`


### 3. Code!

The code to read DHT22 data is on RaspberryDHT22.py file in this repository.

Important: To reading data from sensor works, you must have Adafruit Lib in the right directory (same of python class). 
