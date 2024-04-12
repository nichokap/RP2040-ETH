#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Main script

Do your stuff here, this file is similar to the loop() function on Arduino

Create a Modbus RTU client (slave) which can be requested for data or set with
specific values by a host device.

The RTU communication pins can be choosen freely (check MicroPython device/
port specific limitations).
The register definitions of the client as well as its connection settings like
bus address and UART communication speed can be defined by the user.
"""

# import modbus client classes
from umodbus.serial import ModbusRTU
from machine import UART, Pin
from time import sleep

IS_DOCKER_MICROPYTHON = False
try:
    import machine
    machine.reset_cause()
except ImportError:
    raise Exception('Unable to import machine, are all fakes available?')
except AttributeError:
    # machine fake class has no "reset_cause" function
    IS_DOCKER_MICROPYTHON = True
    import json





# ===============================================
# RTU Slave setup
# act as client, provide Modbus data via RTU to a host device
# ModbusRTU can get serial requests from a host device to provide/set data
# check MicroPython UART documentation
# https://docs.micropython.org/en/latest/library/machine.UART.html
# for Device/Port specific setup
#
# RP2 needs "rtu_pins = (Pin(4), Pin(5))" whereas ESP32 can use any pin
# the following example is for an ESP32.
# For further details check the latest MicroPython Modbus RTU documentation
# example https://micropython-modbus.readthedocs.io/en/latest/EXAMPLES.html#rtu
rtu_pins = (20, 21)         # (TX, RX)
slave_addr = 10             # address on bus as client
baudrate = 9600
uart_id = 1

print('Using pins {} with UART ID {}'.format(rtu_pins, uart_id))

client = ModbusRTU(
    addr=slave_addr,        # address on bus
    pins=rtu_pins,          # given as tuple (TX, RX)
    baudrate=baudrate,      # optional, default 9600
    # data_bits=8,          # optional, default 8
    # stop_bits=1,          # optional, default 1
    # parity=None,          # optional, default None
    # ctrl_pin=12,          # optional, control DE/RE
    uart_id=uart_id         # optional, default 1, see port specific docs
)




if IS_DOCKER_MICROPYTHON:
    # works only with fake machine UART
    assert client._itf._uart._is_server is True


def reset_data_registers_cb(reg_type, address, val):
    # usage of global isn't great, but okay for an example
    global client
    global register_definitions

    print('Resetting register data to default values ...')
    client.setup_registers(registers=register_definitions)
    print('Default values restored')


doorcontact = Pin(6,Pin.IN,Pin.PULL_UP)
print('The initial door contact status is:')
print(doorcontact.value())

# common slave register setup, to be used with the Master example above
register_definitions = {
    "ISTS": {
        "DOOR_STATUS": {
            "register": 67,
            "len": 1,
            "val": doorcontact.value()
        }
    }
}

# alternatively the register definitions can also be loaded from a JSON file
# this is always done if Docker is used for testing purpose in order to keep
# the client registers in sync with the test registers
if IS_DOCKER_MICROPYTHON:
    with open('registers/example.json', 'r') as file:
        register_definitions = json.load(file)

# reset all registers back to their default value with a callback
register_definitions['ISTS']['DOOR_STATUS']['val'] = doorcontact.value()

print('Setting up registers ...')
# use the defined values of each register type provided by register_definitions
client.setup_registers(registers=register_definitions)
# alternatively use dummy default values (True for bool regs, 999 otherwise)
# client.setup_registers(registers=register_definitions, use_default_vals=True)
print('Register setup done')

print('Serving as RTU client on address {} at {} baud'.
      format(slave_addr, baudrate))


while True:
    register_definitions['ISTS']['DOOR_STATUS']['val'] = doorcontact.value()
    client.setup_registers(registers=register_definitions)
    try:
        result = client.process()
    except KeyboardInterrupt:
        print('KeyboardInterrupt, stopping RTU client...')
        break
    except Exception as e:
        print('Exception during execution: {}'.format(e))
    sleep(0.2)
    print(doorcontact.value())
print("Finished providing/accepting data as client")
