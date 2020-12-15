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
    for s in split:
        starting_numbers.append(int(s))

    numbers = {}
    for i in range(0,len(starting_numbers) - 1):
        numbers[starting_numbers[i]] = i + 1
    i = len(starting_numbers)
    latest = starting_numbers[-1]
    while i < 2020:
        latest = iterate(numbers, latest,i)
        i+=1
    print("Part 1: %d" % latest)  
    
    numbers2 = {}
    for i in range(0,len(starting_numbers) - 1):
        numbers2[starting_numbers[i]] = i + 1
    i = len(starting_numbers)
    latest = starting_numbers[-1]
    last_zero = 0
    while i < 30000000:
        latest = iterate(numbers2, latest, i)
        i+=1
    print("Part 2: %d" % latest)
    
    

    