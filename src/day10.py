#day10.py

def recurse(entries, index, cache):
    if(cache[index] > -1):
        return cache[index]
    max_joltage = entries[index] + 3
    i = index + 1
    leaf_nodes = 0
    while i < len(entries) and entries[i] <= max_joltage:
        leaf_nodes += recurse(entries, i, cache)
        i += 1
    cache[index] = leaf_nodes
    return leaf_nodes

def day10(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    entries = [];
    
    for line in lines:
        entries.append(int(line))
    
    entries.sort()
    last_joltage = 0
    count1 = 0
    count3 = 0
    for entry in entries:
        if entry - last_joltage == 3:
            count3 += 1
        elif entry - last_joltage == 1:
            count1 += 1
        last_joltage = entry
    count3 += 1 # final adapter
    
    part1 = count1 * count3
    print("Part 1: %d" % part1)

    entries.insert(0, 0) # outlet is the root of the tree
    cache = [-1] * len(entries)
    cache[len(cache) - 1] = 1 # final adapter returns a leaf node count of 1
    part2 = recurse(entries, 0, cache)
    print("Part 2: %d" % part2)
    