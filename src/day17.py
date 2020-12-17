#day17.py

from collections import defaultdict

def dimensions2(gridA):
    min_w = max_w = min_z = max_z = min_y = max_y = min_x = max_x = 0
    for w in gridA:
        if w < min_w:
            min_w = w
        elif w > max_w:
            max_w = w
        for z in gridA[w]:
            if z < min_z:
                min_z = z
            elif z > max_z:
                max_z = z
            for y in gridA[w][z]:
                if y < min_y:
                    min_y = y
                elif y > max_y:
                    max_y = y
                for x in gridA[w][z][y]:
                    if x < min_x:
                        min_x = x
                    elif x > max_x:
                        max_x = x
    return min_w, max_w, min_z, max_z, min_y, max_y, min_x, max_x

def dimensions(gridA):
    min_z = max_z = min_y = max_y = min_x = max_x = 0
    for z in gridA:
        if z < min_z:
            min_z = z
        elif z > max_z:
            max_z = z
        for y in gridA[z]:
            if y < min_y:
                min_y = y
            elif y > max_y:
                max_y = y
            for x in gridA[z][y]:
                if x < min_x:
                    min_x = x
                elif x > max_x:
                    max_x = x
    return min_z, max_z, min_y, max_y, min_x, max_x

def evalpos2(gridA, w, z, y, x):
    active_neighbors = 0
    for w1 in range(w-1,w+2):
        for z1 in range(z-1,z+2):
            for y1 in range(y-1, y+2):
                for x1 in range(x-1, x+2):
                    if w1 == w and z1 == z and y1 == y and x1 == x:
                        continue
                    if(gridA[w1][z1][y1][x1]):
                        active_neighbors+=1
    if gridA[w][z][y][x] and (active_neighbors == 2 or active_neighbors == 3):
        return True
    elif not gridA[w][z][y][x] and active_neighbors == 3:
        return True
    return False


def evalpos(gridA, z, y, x):
    active_neighbors = 0
    for z1 in range(z-1,z+2):
        for y1 in range(y-1, y+2):
            for x1 in range(x-1, x+2):
                if z1 == z and y1 == y and x1 == x:
                    continue
                if(gridA[z1][y1][x1]):
                    active_neighbors+=1
    if gridA[z][y][x] and (active_neighbors == 2 or active_neighbors == 3):
        return True
    elif not gridA[z][y][x] and active_neighbors == 3:
        return True
    return False

def count_active2(gridA):
    min_w, max_w, min_z, max_z, min_y, max_y, min_x, max_x = dimensions2(gridA)
    count = 0
    for w in range(min_w, max_w + 1):
        for z in range(min_z, max_z + 1):
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    if(gridA[w][z][y][x]):
                        count += 1
    return count

def count_active(gridA):
    min_z, max_z, min_y, max_y, min_x, max_x = dimensions(gridA)
    count = 0
    for z in range(min_z, max_z + 1):
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if(gridA[z][y][x]):
                    count += 1
    return count

def iterate2(gridA, gridB):
    gridB.clear()
    min_w, max_w, min_z, max_z, min_y, max_y, min_x, max_x = dimensions2(gridA)
    for w in range(min_w - 1, max_w + 2):
        for z in range(min_z - 1, max_z + 2):
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    gridB[w][z][y][x] = evalpos2(gridA, w, z, y, x)    

def iterate1(gridA, gridB):
    gridB.clear()
    min_z, max_z, min_y, max_y, min_x, max_x = dimensions(gridA)
    for z in range(min_z - 1, max_z + 2):
        for y in range(min_y - 1, max_y + 2):
            for x in range(min_x - 1, max_x + 2):
                gridB[z][y][x] = evalpos(gridA, z, y, x)
    
def multi_dict(K, type): 
    if K == 1: 
        return defaultdict(type) 
    else: 
        return defaultdict(lambda: multi_dict(K-1, type)) 

def day17(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    starting_grid = multi_dict(3, bool)
    
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if(lines[i][j] == '\n'):
                continue
            starting_grid[0][i][j] = (lines[i][j] == '#')
    
    
    gridA = starting_grid.copy()
    gridB = starting_grid.copy()
    
    for i in range(0, 6+1):
        if i % 2 == 0:
            iterate1(gridA, gridB)
        else:
            iterate1(gridB, gridA)
    
    print("Part 1: %d" % count_active(gridA))
    
    gridA2 = multi_dict(4, bool)
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if(lines[i][j] == '\n'):
                continue
            gridA2[0][0][i][j] = starting_grid[0][i][j]
    
    gridB2 = gridA2.copy()
    
    for i in range(0, 6+1):
        if i % 2 == 0:
            iterate2(gridA2, gridB2)
        else:
            iterate2(gridB2, gridA2)
            
    print("Part 2: %d" % count_active2(gridA2))
   