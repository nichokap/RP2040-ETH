from machine import Pin
from neopixel import NeoPixel


#Configure the built-in WS2812 LED pins of RP2040-ETH and set the number of LEDs to 1
strip = NeoPixel(Pin(25), 1)

#Set the color of the first and only LED
strip[0] = (0,150,0) # color codes in GRB (Green=0, Red=150, Blue=0)

#command to write the color to the LED
strip.write()
