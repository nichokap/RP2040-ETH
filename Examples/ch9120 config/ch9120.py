from machine import UART, Pin
import time

class CH9120:
    def __init__(self, uart):
        self.uart = uart
        self.MODE = 0  #0:TCP Server 1:TCP Client 2:UDP Server 3:UDP Client
        self.GATEWAY = (192, 168, 1, 1)    # GATEWAY
        self.TARGET_IP = (192, 168, 1, 200)  # TARGET_IP 
        self.LOCAL_IP = (192, 168, 1, 133) # LOCAL_IP
        self.SUBNET_MASK = (255,255,252,0)  # SUBNET_MASK
        self.LOCAL_PORT = 1000              # LOCAL_PORT1
        self.TARGET_PORT = 1883             # TARGET_PORT
        self.BAUD_RATE = 115200             # BAUD_RATE
        self.CFG = Pin(18, Pin.OUT,Pin.PULL_UP)
        self.RST = Pin(19, Pin.OUT,Pin.PULL_UP)
            
    def enter_config(self):
        print("begin")
        self.RST.value(1)
        self.CFG.value(0)
        time.sleep(0.5)
    
    def exit_config(self):
        self.uart.write(b'\x57\xab\x0D')
        time.sleep(0.1)
        self.uart.write(b'\x57\xab\x0E')
        time.sleep(0.1)
        self.uart.write(b'\x57\xab\x5E')
        time.sleep(0.1)
        self.CFG.value(1)
        time.sleep(0.1)
        print("end")
    
    def set_mode(self,MODE):
        self.MODE = MODE
        self.uart.write(b'\x57\xab\x10' + self.MODE.to_bytes(1, 'little'))#Convert int to bytes
        time.sleep(0.1)
        
    def set_localIP(self,LOCAL_IP):
        self.LOCAL_IP = LOCAL_IP
        self.uart.write(b'\x57\xab\x11' + bytes(self.LOCAL_IP))#Converts the int tuple to bytes
        time.sleep(0.1)
        
    def set_subnetMask(self,SUBNET_MASK):
        self.SUBNET_MASK = SUBNET_MASK
        self.uart.write(b'\x57\xab\x12' + bytes(self.SUBNET_MASK))
        time.sleep(0.1)
        
    def set_gateway(self,GATEWAY):
        self.GATEWAY = GATEWAY
        self.uart.write(b'\x57\xab\x13' + bytes(self.GATEWAY))
        time.sleep(0.1)
        
    def set_localPort(self,LOCAL_PORT):
        self.LOCAL_PORT = LOCAL_PORT
        self.uart.write(b'\x57\xab\x14' + self.LOCAL_PORT.to_bytes(2, 'little'))
        time.sleep(0.1)
        
    def set_targetIP(self,TARGET_IP):
        self.TARGET_IP = TARGET_IP
        self.uart.write(b'\x57\xab\x15' + bytes(self.TARGET_IP))
        time.sleep(0.1)
        
    def set_targetPort(self,TARGET_PORT):
        self.TARGET_PORT = TARGET_PORT
        self.uart.write(b'\x57\xab\x16' + self.TARGET_PORT.to_bytes(2, 'little'))
        time.sleep(0.1)
        
    def set_baudRate(self,BAUD_RATE):
        self.BAUD_RATE = BAUD_RATE
        self.uart.write(b'\x57\xab\x21' + self.BAUD_RATE.to_bytes(4, 'little'))
        time.sleep(0.1)
    
