#util.py

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