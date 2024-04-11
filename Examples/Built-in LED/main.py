from machine import Pin
from neopixel import NeoPixel


#Configure the built-in LED
strip = NeoPixel(Pin(25), 1)
strip[0] = (0,150,0) # color codes in RGB
strip.write()
