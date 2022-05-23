# Blink LED program for Adafruit Grand Central

import board
import digitalio
import time

# Set up the digital IO

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Loop while blinking

while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)