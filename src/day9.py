#day9.py

blocksize = 25

def day9(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    entries = []
    for line in lines:
        entries.append(int(line))
    
    part1 = -1;
    for i in range(blocksize,len(entries)):
        found = False
        for j in range(1,blocksize + 1):
            for k in range(2,blocksize + 1):
                if k == j:
                    continue
                if entries[i] == entries[i - j] + entries[i - k]:
                    found = True
                    break
        if not found:
            part1 = entries[i]
            break
    
    print("Part 1: %d" % part1)

    part2 = -1
    for i in range(0, len(entries) - 1):
        sum = entries[i]
        for j in range(1, len(entries) - i):
            sum += entries[i+j]
            if sum == part1:
                max = entries[i]
                min = entries[i]
                for k in range(i,i+j):
                    if entries[k] > max:
                        max = entries[k]
                    if entries[k] < min:
                        min = entries[k]
                part2 = max + min
                break
            elif sum > part1:
                break
        if part2 > -1:
            break
            
    print("Part 2: %d" % part2)
    
    