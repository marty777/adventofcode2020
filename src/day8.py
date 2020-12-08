#day8.py

class Program:
    def __init__(self, acc, addr):
        self.acc = 0
        self.addr = 0
        self.prog = []
        self.terminated = False
    def set_program(self, program):
        self.prog.clear();
        for inst in program:
            self.prog.append(inst)
        for inst in self.prog:
            inst.count = 0
        self.acc = 0
        self.addr = 0
        self.terminated = False
    def set_acc(self, acc):    
        self.acc = acc
    def loop_found(self):
        for inst in self.prog:
            if inst.count > 1:
                return True
        return False
    def execute(self):
        if self.terminated:
            return
        self.prog[self.addr].count += 1
        if self.prog[self.addr].inst == 'acc':
            self.acc += self.prog[self.addr].val
            self.addr += 1
        elif self.prog[self.addr].inst == 'jmp':
            self.addr += self.prog[self.addr].val
        elif self.prog[self.addr].inst == 'nop':
            self.addr += 1
        
        if self.addr >= len(self.prog):
            self.terminated = True

class Instruction:
    def __init__(self, inst, val):
        self.inst = inst;
        self.val = int(val);
        self.count = 0

def inst_copy(in_prog, out_prog):
    out_prog.clear()
    for inst in in_prog:
        out_prog.append(Instruction(inst.inst, inst.val));

def day8(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    instructions = [];
    max_index = 0
    
    program1 = Program(0,0)
    
    for line in lines:
        line2 = line[0:-1] #omit newline
        split = line2.split(' ')
        instructions.append(Instruction(split[0], split[1]))
    
    program1.set_program(instructions)
    
    last_acc = 0
    while not program1.loop_found():
        last_acc = program1.acc
        program1.execute()

    print("Part 1: %d" % last_acc)
    
    program2 = Program(0,0);
    for i in range(0,len(instructions)):
        
        instructions2 = []
        inst_copy(instructions, instructions2)
        if instructions2[i].inst == 'nop':
            instructions2[i].inst = 'jmp'
        elif instructions2[i].inst == 'jmp':
            instructions2[i].inst = 'nop'
        program2.set_program(instructions2)
        count = 0;
        while not program2.loop_found() and not program2.terminated:
            program2.execute()
            count += 1
        if program2.terminated:
            print("Part 2: %d" % program2.acc)
            break
    
    
        
    
    
    
    
    
    