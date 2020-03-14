import time
import multiprocessing as mp
import queue

keystream = "0xd30xea0x3d0x6a"


def RC8(state, key, n):
    yield state & 0xff

    for _ in range(8):
        c, s = key, state
        b = 0
        while c:
            b^= c&1 * s&1
            c >>=1; s >>=1
        state = state >> 1 | b << 63
    n-=1

def FuzzWorker(start, end):
    print("test")
    for i in range(9999):
        output = ""
        for j in range(start, end):
            for z, x in enumerate(RC8(j, i, 4)):
                output += hex(x)
            if output == keystream:
                print("MATCH FOUND! SEED: " + str(j) + " KEY: " + str(i))
    return

def main():
    mp.set_start_method('spawn')
    q = mp.Queue()
    start = 0
    end = 999
    for _ in range(9):
        p = mp.Process(target=FuzzWorker, args=(start,end))
        p.start()
        start += 1000
        end += 1000


if __name__ == "__main__":
    main()