#day15.py

def iterate(numbers, previous, i):
    if previous in numbers:
        last = numbers[previous]
        numbers[previous] = i
        return i - last
    else:
        numbers[previous] = i
        return 0

def day15(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    starting_numbers = []
    
    line = lines[0]
    split = line.split(',')
    
    numbers = {}
    for i in range(0, len(split)):
        numbers[int(split[i])] = i + 1
    
    i = len(split)
    latest = int(split[-1])
    while i < 30000000:
        latest = iterate(numbers, latest,i)
        if i == 2020 - 1:
            print("Part 1: %d" % latest)
                   
        i+=1
    print("Part 2: %d" % latest)
    