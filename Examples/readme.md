To try the examples you first need to install a micropython firmware to your board.
Please look <a href="https://github.com/nichokap/RP2040-ETH/tree/main/MicroPython%20Firmware">here</a>

### 1. Built-in LED

In this example I just control the built-in LED of the RP2040-ETH chip

### 2. Configure the CH9120 chip

In this example I created a boot.py and used the provided ch9120.py library from the official <a href="https://www.waveshare.com/wiki/RP2040-ETH">waveshare wiki</a> to initialize the ch9120 serial to ethernet converter as a TCP server.

### 3. Control built-in LED though TCP
In this example the RP2040-ETH is programmed to receive simple characters over TCP to control its built-in LED.
The boot.py and ch9120.py files from Example 2 need to be used along with the main.py in order for the ch9120 chip to be initialized properly.

To test the operation you can download and use the freeware [Hercules SETUP utility](https://www.hw-group.com/software/hercules-setup-utility) on your computer and test following the below steps:

1. Choose the TCP Client tab
2. In TCP Module IP and Port set the IP and Port setting of the boot.py file as set on your RP2040-ETH
3. Click on Ping. If you see "Received ICMP ECHO Reply" the connection to the RP2040-ETH is successful.
4. Then click on Connect
5. Every second you should receive a t character.
6. Try to send the "f" character by writing on the first row of the Send section and clicking the Send button. (HEX should stay unclicked).The built-in LED of the RP2040-ETH should turn off.
8. Try to send the "n" character by writing on the first row of the Send section and clicking the Send button. (HEX should stay unclicked).The built-in LED of the RP2040-ETH should turn on.

![HerculesSetupTool](https://github.com/nichokap/RP2040-ETH/blob/main/Examples/3.%20Control%20built-in%20LED%20with%20TCP%20commands/HerculesTcpClientTool.PNG?raw=true)

### 4. Modbus RTU over TCP (encapsulated) client
This is just a port of the [rtu_client_example.py](https://github.com/brainelectronics/micropython-modbus/blob/develop/examples/rtu_client_example.py) of the [brainelectronics
/micropython-modbus](https://github.com/brainelectronics/micropython-modbus) that is modified to use the the RP2040-ETH pins 20 and 21, i.e. the built-in pins connected from the RP2040 chip to the CH9120 serial to ethernet converter chip. 
The boot.py and ch9120.py files from Example 2 need to be used along with the main.py in order for the ch9120 chip to be initialized properly.

### 5. Modbus client - Pin status as Input Register
This is just a modification of the Example 4 that reads the status of Pin 6 and responds the value as Input Register.
