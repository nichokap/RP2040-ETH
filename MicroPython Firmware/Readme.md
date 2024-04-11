For my projects, I am using the official Raspberry Pi Pico MicroPython firmware 20240222-v1.22.2 

# Manual Installation
The firmware can be downloaded from the official Raspberry Pi Pico website, i.e. <a href="https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2">here</a>.

A copy of the UF2 file can be found also on this folder as well.

Flashing instructions are available <a href="https://www.raspberrypi.com/documentation/microcontrollers/micropython.html">here</a>.

# Micropython installation through <a href="https://thonny.org/">Thonny </a>

A more friendly installation process is available through Thonny. Here are the instruction:

1. Connecth the RP2040-ETH to your computer by pressing down the BOOT button.
2. Open Thonny and go to Run --> Configure Interpreter
3. Click on the Install of Update Micropython link
4. On the Target Volume select the drive of the RP2040-ETH
5. On the MicroPython family select RP2
6. On the variant select Raspberry Pi Pico / Pico H
7. on the version select the latest, in my case I am using the 1.22.2
8. Click install and wait for the board to reset
