import time
import multiprocessing as mp
import queue
import sys
keystream_long = b"\xd3\xea\x3d\x6a\x8d\x66\xee\x30\x5f\xf4\x22\x9e\xc9\xd9\x00\xc6"
keystream = "0xd30xea0x3d0x6a"
answer = ""

def rc8(state, key, n):
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

def FuzzWorker(start, end, id):
    print("WORKER PROCESS " + str(id) + " STARTING RANGE: " + str(start) + " TO " + str(end))
    for i in range(9999):
        output = ""
        print("WORKER PROCESS " + str(id) + " ATTEMPT: " + str(i) + " OF 9999 \n")
        for j in range(start, end):
            for _, x in enumerate(rc8(i, j, 4)):
                output += hex(x)
            if output == keystream:
                answer = "MATCH FOUND! SEED: " + str(j) + " KEY: " + str(i)
                print(answer)
    return

def main():
    start = 0
    end = 999

    for _ in range(10):
        p = mp.Process(target=FuzzWorker, args=(start,end, _))
        p.start()
        start += 1000
        end += 1000


if __name__ == "__main__":
    main()