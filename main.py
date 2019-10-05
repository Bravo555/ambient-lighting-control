#!/usr/bin/python3

import serial
import os
import sys

PORT = 'COM4' if os.name == 'nt' else '/dev/ttyUSB0'


def set_brightness(args):
    brightness = bytes.fromhex(args.pop(0))
    if len(brightness) > 1:
        print('brightness should be in range 00-ff')
        sys.exit(2)
    return b'\x02' + brightness


def enable(args):
    return b'\x01\xff'


def disable(args):
    return b'\x01\x00'


def set_mode(args):
    mode = args.pop(0)
    payload = b'\x04'
    if mode == 'capture':
        return payload + b'\xff'
    elif mode == 'ambient':
        return payload + b'\x00'
    else:
        return b''


payloads = {
    'enable': enable,
    'disable': disable,
    'brightness': set_brightness,
    'mode': set_mode
}

if __name__ == '__main__':
    ser = serial.Serial(PORT, 115200)

    if len(sys.argv) < 2:
        print('Usage: lightctl command [args]')
        sys.exit(1)

    command, *args = sys.argv[1:]

    payload = payloads[command](args)
    ser.write(payload)
