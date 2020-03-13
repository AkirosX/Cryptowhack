#!/usr/bin/env python3
import sys

def rc8(state, key, n):
    '''
    Top Secret RC8 Stream Cipher
    '''
    z = 8
    while (z > 0):
        #return state logically AND-ed with 0xff, this trims off all but the last 8 bits (a single byte) and sends it back to the callee to be xor'd with the plaintext
        #print("STATE: " + str(state & 0xff))
        yield state & 0xff
        #perform the following tasks 8 times
        for _ in range(8):
            #Assign Key and State to temporary variables C and S respectively
            c, s = key, state
            b = 0
            while c:
                #if C is odd, then C=1, if C is even, then C=0
                #if S is odd, then S=1, if S is even, then S=0
                #multiply C and S together (can only be 0x1, 1x0, 0x0, or 1x1) // there is a 1 in 4 chance that the result will be 1
                #XOR the result with b
                b ^= c & 1 * s & 1
                # Divide C by 2. Divide S by 2
                c >>= 1 ; s >>= 1
            state = state >> 1 | b << 63
        z -= 1

# EXTRACTED KEYSTREAM FROM KNOWN PLAINTEXT IS: d3ea3d6a

def main():
    seed, key = 12345678, 999999999 # Missing

  #  with open(sys.argv[1], 'rb') as fin:
  #     data = bytearray(fin.read())

    for i,x in enumerate(rc8(seed, key, len(data))):
#       print("KEYSTREAM: " + hex(x))
        #print("\n FINALKS: " + str(x))
        data[i] ^= x
#       print("IN: " + chr(old) + "    |    " + hex(old) + "\n" + "KSBYTE: " + hex(x)  + "\n" + "OUT: " + chr(data[i]) + "    |    " + hex(data[i]) + "\n")

if __name__ == "__main__":
    main()