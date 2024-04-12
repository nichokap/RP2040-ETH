from machine import Pin,UART
from neopixel import NeoPixel
import time

#Configure the built-in WS2812 LED pins of RP2040-ETH and set the number of LEDs to 1
strip = NeoPixel(Pin(25), 1)

#Set a UART connection on Pins 20 and 21, i.e. the built-in pins connected from the RP2040 chip to the CH9120 serial to ethernet converter chip.
uart = UART(1, baudrate=9600, tx=Pin(20), rx=Pin(21))
uart.init(bits=8, parity=None, stop=2)


while True:
    uart.write('t') #this way the client will constantly receive a t character to confirm that a connection exists
    if uart.any(): 
        data = uart.read() 
        #if the RP2040-ETH receives the caracter "n" then the built in LED lits blue
        if data== b'n': 
            strip[0] = (0,0,150) 
            strip.write()
        #if the RP2040-ETH receives the caracter "f" then the built in LED turns off
        if data== b'f':
            strip[0] = (0,0,0)
            strip.write()
    time.sleep(1)
