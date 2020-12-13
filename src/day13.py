#day13.py

from math import gcd
from fractions import gcd

def divisible(x, y):
    return ((y % x) == 0)
    
def extended_gcd(a, b):
    last_r = a
    curr_r = b
    last_s = 1
    curr_s = 0
    last_t = 0
    curr_t = 1
    i = 1
    while(curr_r != 0):
        q = int(last_r/curr_r)
        next_r = last_r - q * curr_r
        next_s = last_s - q * curr_s
        next_t = last_t - q * curr_t
        
        last_r = curr_r
        curr_r = next_r
        last_s = curr_s
        curr_s = next_s
        last_t = curr_t
        curr_t = next_t
        
        i+=1
    g = last_r
    u = last_s
    v = last_t
    return(g, u, v)
        
def day13(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    
    start = int(lines[0]);
    schedule = lines[1];
    
    buses = []
    bus_pos = []
    schedule_split = schedule.split(',')
    i = -1
    for entry in schedule_split:
        i += 1
        if(entry == 'x'):
            continue
        buses.append(int(entry))
        bus_pos.append(i)
   
    index = start
    thebus = 0
    done = False
    while not done:
        for bus in buses:
            if divisible(bus, index):
                thebus = bus
                done = True
                break
        index += 1
    
    print("Part 1: %d" % ((index - start - 1) * thebus))
    
    # chinese remainder theorem solution using extended GCD
    last_modulus = buses[0]
    last_remainder = bus_pos[0]
    for i in range(1,len(buses)):
        g,u,v = extended_gcd(last_modulus, buses[i])
        last_remainder = v * buses[i] * last_remainder + u * last_modulus * bus_pos[i]
        last_modulus *= buses[i]  
        
    part2 = last_modulus - (last_remainder % last_modulus)     
    print("Part 2: %d" % (part2))
        
   

    