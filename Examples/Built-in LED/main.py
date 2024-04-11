from machine import Pin
from neopixel import NeoPixel


#Configure the built-in WS2812 LED pins and set the number of LEDs to 1
strip = NeoPixel(Pin(25), 1)

#Set the color of the first and only LED
strip[0] = (0,150,0) # color codes in RGB

#command to write the color to the LED
strip.write()
