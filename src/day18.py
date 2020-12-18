#day18.py

class MathNode:
    def __init__(self, string):
        self.op = '+'
        self.left = ''
        self.right = ''
        self.op = '+'
        self.val = 0

def digit(symbol):
    return(symbol >= '0' and symbol <= '9')

def symbol_count(symbols, symbol):
    count = 0
    for i in range(0, len(symbols)):
        if(symbols[i] == symbol):
            count += 1
    return count

def recurse(symbols, part):
    # first resolve brackets
    # if part == 1 - resolve + and * in order
    # if part == 2 then resolve + then resolve *
    index = 0
    while index < len(symbols):
        nesting = 0
        if symbols[index] == '(':
            nesting += 1
            index2 = index + 1
            while index2 < len(symbols):
                if symbols[index2] == '(':
                    nesting += 1
                elif symbols[index2] == ')':
                    nesting -=1
                if nesting == 0:
                    val = recurse(symbols[index+1:index2], part)
                    del symbols[index:index2+1]
                    symbols.insert(index,str(val))
                    index -=1
                    break
                index2 += 1
        index += 1
        if index >= len(symbols):
            if symbol_count(symbols, '(') > 0:
                index = 0
    if(part == 1):
        index = 0
        while index < len(symbols):
            if(symbols[index] == '+'):
                val = int(symbols[index-1]) + int(symbols[index+1])
                del symbols[index-1:index+2]
                symbols.insert(index-1, str(val))
                index -=1
            elif(symbols[index] == '*'):
                val = int(symbols[index-1]) * int(symbols[index+1])
                del symbols[index-1:index+2]
                symbols.insert(index-1, str(val))
                index -=1
            index += 1
    elif(part == 2):
        index = 0
        while index < len(symbols):
            if(symbols[index] == '+'):
                val = int(symbols[index-1]) + int(symbols[index+1])
                del symbols[index-1:index+2]
                symbols.insert(index-1, str(val))
                index -=1
            index += 1
            
        index = 0
        while index < len(symbols):
            if(symbols[index] == '*'):
                val = int(symbols[index-1]) * int(symbols[index+1])
                del symbols[index-1:index+2]
                symbols.insert(index-1, str(val))
                index -=1
            index += 1
    return int(symbols[0])

def eval(start_line, mode):
    # parse into symbols
    symbols = []
    index = 0
    while index < len(start_line):
        if start_line[index] == '\n' or start_line[index] == ' ':
            index += 1
            continue
        if(digit(start_line[index])):
            i2 = index
            while i2 < len(start_line) and digit(start_line[i2]):
                i2 += 1
            symbols.append(start_line[index:i2])
            index = i2
        else:
            symbols.append(start_line[index])
            index += 1
    return recurse(symbols, mode)

def day18(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    
    i = 0
    sum = 0
    for line in lines:
        sum += eval(line, 1)
        i+=1
    print("Part 1: %d" % sum)
    
    sum = 0
    for line in lines:
        sum += eval(line, 2)
        i+=1
    print("Part 2: %d" % sum)
    
    