#day8.py

from src.util import Program, Instruction, inst_copy

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
        else:
            continue
        program2.set_program(instructions2)
        while not program2.loop_found() and not program2.terminated:
            program2.execute()
        if program2.terminated:
            print("Part 2: %d" % program2.acc)
            break
    