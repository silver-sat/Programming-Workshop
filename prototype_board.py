# Avionics Board as an object
#

import inspect

class PrototypeBoard():
    description = "Board Prototype"
    def describe():
        print(f"Description: {PrototypeBoard.description}")
        print(f"Processor: {board.processor}")
    
board = PrototypeBoard()

board.name = "Avionics Board"
board.processor = "SAMD21"
board.GNC = "Adafruit MPU 6050"
board.watchdog_timer = "TPS3813-Q1"
board.FRAM = "CY15B256J"
board.real_time_clock = "DS1337"

class PrototypeBoard():
        

