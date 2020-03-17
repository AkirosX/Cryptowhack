#!/usr/bin/env python3
import sys

def rc8(state, key, n):
    '''
    Top Secret RC8 Stream Cipher
    '''
    while (n > 0):
        yield state & 0xff
        for _ in range(8):
            c, s = key, state
            b = 0
            while c:
                b ^= c & 1 * s & 1
                c >>= 1 ; s >>= 1
            state = state >> 1 | b << 63
        n -= 1


output = ""
for _, x in enumerate(rc8(1782442707, 235235235235352525253235, 4)):
    output += hex(x) 
print(output + "\n")