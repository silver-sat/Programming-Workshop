# Log data from accelerometer to file
#
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import digitalio
import adafruit_adxl34x
import mount_sd

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
i2c = board.I2C()  # uses board.SCL and board.SDA
accelerometer = adafruit_adxl34x.ADXL345(i2c)
file_name = "/sd/adxl345_log.txt"

print(f'Logging ADXL345 accelerometer data to file {file_name}')

# Read and count

while True:
    with open(file_name, 'a') as open_file:
        led.value = True
        x, y, z = accelerometer.acceleration
        output_string = f'{x:10.5f}{y:10.5f}{z:10.5f}'
        print(output_string)        
        open_file.write(output_string)
        led.value = False

    time.sleep(1.0)
