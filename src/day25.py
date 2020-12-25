#day25.py

import math

# Baby-step giant-step algorithm for attempting to solve the discrete logarithm problem
# adapted from https://en.wikipedia.org/wiki/Baby-step_giant-step
def babystep_giantstep(base,target,modulus):
    m = 1 + int(math.sqrt(modulus))
    baby_steps = {}
    baby_step = 1
    for r in range(0,m):
        baby_steps[pow(base, r, modulus)] = r
    giant_stride = pow(base,(modulus-2)*m,modulus)
    giant_step = target
    for q in range(0,m):
        if giant_step in baby_steps:
            return q*m + baby_steps[giant_step]
        else:
            giant_step = giant_step * giant_stride % modulus
    return -1

def day25(infile):
    f = open(infile, 'r')
    lines = f.read().splitlines()
    
    card_public_key = int(lines[0])
    door_public_key = int(lines[1])
    
    card_loop_size = babystep_giantstep(7, card_public_key, 20201227)
    if(card_loop_size < 0):
        print("No solution found")
        return
    
    encryption_key = pow(door_public_key, card_loop_size, 20201227)
    print("Solution: %d" % encryption_key)
    