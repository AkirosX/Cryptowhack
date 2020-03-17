keystream = "d3 ea 3d 6a"

keystream_maybe = "d3 ea 3d 6a 8d 66 ee 30 5f f4 22 9e c9 d9 00 c6"

def RC8(state, key, n):
    while (n > 0):
        yield state & 0xff
        for _ in range(8):
            c, s = key, state
            b = 0
            while c:
                b^= c&1 * s&1
                c >>= 1; s >>= 1
            state = state >> 1 | b << 63
        n-=1



output = ""
for _, x in enumerate(RC8(1782442707, 2142141124, 4)):
    output += hex(x) 
print(output + "\n")
    # if output == keystream:
    #     print("MATCH FOUND! SEED: " + str(j) + " KEY: " + str(i))