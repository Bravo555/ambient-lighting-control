#!/usr/bin/python3

import serial
import sys

payloads = {
    'enable': b'\x01\xff',
    'disable': b'\x01\x00'
}

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0')
    print(ser.name)

    command, *args = sys.argv[1:]

    payload = payloads[command]
    ser.write(payload)
