#day11.py
#floor = 0
#occupied = 1
#empty = 2

def projection(gridA, x, y, dx, dy):
    i = y + dy
    j = x + dx
    while i >= 0 and i < len(gridA) and j >= 0 and j < len(gridA[0]):  
        if gridA[i][j] == 1:
           return True
        elif gridA[i][j] == 2:
            return False
        i += dy
        j += dx
    return False

def next_state2(gridA, x, y):
    if gridA[y][x] == 0:
        return 0
    occupied_count = 0
    for i in range(-1, 2):
        for j in range(-1,2):
            if i == 0 and j == 0:
                continue
            if projection(gridA, x, y, j, i):
                occupied_count += 1
    if gridA[y][x] == 1:
        if occupied_count >= 5:
            return 2
    if gridA[y][x] == 2:
        if occupied_count == 0:
            return 1
    return gridA[y][x]

def next_state1(gridA, x, y):
    if gridA[y][x] == 0:
        return 0
    
    occupied_count = 0
    i = max(0,y-1)
    while i <= y+1 and i < len(gridA):
        j = max(0, x-1)
        while j <= x+1 and j < len(gridA[0]):
            if i == y and j == x:
                j += 1
                continue
            if gridA[i][j] == 1:
                occupied_count+=1
            j += 1
        i+=1
    if gridA[y][x] == 1:
        if occupied_count >= 4:
            return 2
    if gridA[y][x] == 2:
        if occupied_count == 0:
            return 1
    return gridA[y][x]

def step1(gridA, gridB):
    for i in range(0,len(gridB)):
        for j in range(0,len(gridB[0])):
            gridB[i][j] = next_state1(gridA, j, i)

def step2(gridA, gridB):
    for i in range(0,len(gridB)):
        for j in range(0,len(gridB[0])):
            gridB[i][j] = next_state2(gridA, j, i)

def dif(gridA, gridB):
    dif_count = 0
    for i in range(0,len(gridB)):
        for j in range(0,len(gridB[0])):
            if(gridA[i][j] != gridB[i][j]):
                dif_count += 1
    return dif_count

def occupied_count(gridA):
    occupied_count = 0
    for i in range(0,len(gridA)):
        for j in range(0,len(gridA[0])):
            if(gridA[i][j] == 1):
                occupied_count += 1
    return occupied_count

def grid_copy(gridA, gridB):
    for i in range(0,len(gridA)):
        for j in range(0,len(gridA[0])):
            gridB[i][j] = (gridA[i][j])

def grid_print(gridA):
    for i in range(0,len(gridA)):
        for j in range(0,len(gridA[0])):
            if gridA[i][j] == 0: 
                print('.', end='')
            elif gridA[i][j] == 1:
                print('#', end='')
            elif gridA[i][j] == 2:
                print('L', end='')
        print("")

def list2d(height, width):
    ret = []
    for i in range(0, height):
        ret.append([0] * width)
    return ret
    
def day11(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    instructions = [];
    max_index = 0
    grid = []
    
    for i in range(0,len(lines)):
        line = lines[i]
        if line[len(line)-1] == '\n':
            line = line[:-1]
        grid.append([0] * (len(line)))
        for j in range(0, len(line)):
            if line[j] == '.':
                grid[i][j] = 0
            elif line[j] == '#':
                grid[i][j] = 1
            elif line[j] == 'L':
                grid[i][j] = 2
    gridA = list2d(len(grid), len(grid[0]))
    gridB = list2d(len(grid), len(grid[0]))
    grid_copy(grid, gridA)
    
    change_count = 1
    occupied = 0
    steps = 0
    while change_count > 0:
        if steps % 2 == 0:
            step1(gridA, gridB)
            occupied = occupied_count(gridB)
        else:
            step1(gridB, gridA)
            occupied = occupied_count(gridA)
        change_count = dif(gridA, gridB)
        steps += 1
    
    print("Part 1: %d" % occupied)
    
    grid_copy(grid, gridA)
    change_count = 1
    steps = 0
    while change_count > 0:
        if steps % 2 == 0:
            step2(gridA, gridB)
            occupied = occupied_count(gridB)
            
        else:
            step2(gridB, gridA)
            occupied = occupied_count(gridA)
        change_count = dif(gridA, gridB)
        steps += 1
    
    print("Part 2: %d" % occupied)