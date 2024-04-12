from machine import UART, Pin
from ch9120 import CH9120
from neopixel import NeoPixel
import time


#Set the Built-In LED to lit RED for easy optical indication that the initialization of the ch9120 chip is starting (for more info see the Built-in LED example)
strip = NeoPixel(Pin(25), 1)
strip[0] = (0,150,0)
strip.write()


#Set the configuration to be sent to the built-in CH9120 Serial to Ethernet chip. For my example I use the TCP Server mode.
MODE = 0  #0:TCP Server 1:TCP Client 2:UDP Server 3:UDP Client
GATEWAY = (192, 168, 1, 1)     # GATEWAY
TARGET_IP = (47, 92, 129, 18)  # TARGET_IP (not important in TCP server mode)
LOCAL_IP = (192, 168, 1, 144)  # LOCAL_IP
SUBNET_MASK = (255,255,255,0)# SUBNET_MASK
LOCAL_PORT1 = 1000             # LOCAL_PORT1
TARGET_PORT = 1883             # TARGET_PORT (not important in TCP server mode)
BAUD_RATE = 9600             # BAUD_RATE default 115200

#Set a UART connection on Pins 20 and 21, i.e. the built-in pins connected from the RP2040 chip to the CH9120 serial to ethernet converter chip.
uart1 = UART(1, baudrate=9600, tx=Pin(20), rx=Pin(21))

def ch9120_configure():
    global uart1
    ch9120 = CH9120(uart1)
    ch9120.enter_config() # enter configuration mode
    ch9120.set_mode(MODE)    
    ch9120.set_localIP(LOCAL_IP)
    ch9120.set_subnetMask(SUBNET_MASK)
    ch9120.set_gateway(GATEWAY)
    ch9120.set_localPort(LOCAL_PORT1)
    ch9120.set_targetIP(TARGET_IP)
    ch9120.set_targetPort(TARGET_PORT)
    ch9120.set_baudRate(BAUD_RATE)
    ch9120.exit_config()  # exit configuration mode
    # Clear cache and de(re)configure uart1
    uart1.read(uart1.any())
    time.sleep(0.5)
    #uart1 = UART(1, baudrate=115200, tx=Pin(20), rx=Pin(21))
    uart1.deinit() #command to distroy the UART connection after the successful sent of the configuration to allow a new UART to be initiated on the main program

#send the defined configuration to the CH9120 chip
ch9120_configure()

#Set the Built-In LED to lit Blue for easy optical indication that the initialization of the ch9120 chip has been finished (for more info see the Built-in LED example)
strip[0] = (0,0,150)
strip.write()
