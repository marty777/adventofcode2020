#day14.py

class Memstruction:
    def __init__(self, line):
        if line[len(line)-1] == '\n':
            line = line[:-1]
        self.addr = 0
        self.mask = 0
        self.val = 0
        self.mask = []
        if "mask" in line:
            self.inst = "mask"
            for i in range(7, len(line)):
                self.mask.insert(0, line[i:i+1])
        else:
            self.inst = "mem"
            self.addr = int(line[line.find("[") + 1:line.find("]")])
            self.val = int(line[line.find("= ") + 1:]);

def run2_addrs(mask, initial_addr):
    num_x = 0
    for i in range(0,36):
        if mask[i] == 'X':
            num_x += 1
    addrs = {}
    for i in range(0, 2<<num_x):
        bits = i
        bit_index = 0
        addr = 0
        for j in range(0,36):
            if mask[j] == 'X':
                bit = i >> bit_index & 1
                bit_index += 1
            elif mask[j] == '1':
                bit = 1
            else:
                bit = initial_addr >> j & 1
            if(bit == 0):
                addr = addr & ~(1 << j)
            else:
                addr = addr | (1 << j)
        addrs[addr] = 1
    return addrs
    
def run1(memstructions, memory):
        curr_mask = []
        for mem in memstructions:
            if(mem.inst == "mask"):
                curr_mask = mem.mask.copy()
            else:
                val = mem.val
                
                for i in range(0,36):
                    if curr_mask[i] == 'X':
                        bit = (mem.val >> i) & 1
                        val = val | (bit << i)
                    elif curr_mask[i] == '1':
                        val = val | (1 << i)
                    else:
                        val = val & ~(1 << i)
                memory[mem.addr] = val
        sum =0
        for key in memory:
            sum += memory[key];
        return sum

def run2(memstructions, memory):
        curr_mask = []
        for mem in memstructions:
            if(mem.inst == "mask"):
                curr_mask = mem.mask.copy()
            else:
                val = mem.val
                addrs = run2_addrs(curr_mask, mem.addr)
                for addr in addrs:
                    memory[addr] = mem.val
        sum =0
        for key in memory:
            sum += memory[key];
        return sum

def day14(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    inst = []
    for line in lines:
        inst.append(Memstruction(line))
        
    memory = {}
    part1 = run1(inst, memory)
    
    print("Part 1: %d" % part1)
    
    memory2 = {}
    part2 = run2(inst, memory2)
    
    print("Part 2: %d" % part2)
    
    

    