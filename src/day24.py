#day24.py

#using this hex grid coordinate scheme: http://devmag.org.za/2013/08/31/geometry-with-hex-coordinates/
def coord_from_moves(moves):
    dirs = {}
    dirs['e'] = [1, 0]
    dirs['se'] = [1, -1]
    dirs['sw'] = [0, -1]
    dirs['w'] = [-1, 0]
    dirs['nw'] = [-1, 1]
    dirs['ne'] = [0, 1]
    dx = 0
    dy = 0
    for m in moves:
        dx += dirs[m][0]
        dy += dirs[m][1]
    return dx, dy
    
def hex_bounds(hex):
    min_x = max_x = min_y = max_y = 0
    for coords in hex:
        if hex[coords] % 2 == 0:
            continue
        split = coords.split(',')
        x = int(split[0])
        y = int(split[1])
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    min_x -= 1
    max_x += 1
    min_y -= 1
    max_y += 1
    return min_x, max_x, min_y, max_y

def follow_line(line, seen):
    moves = []
    dirs = ['e', 'se', 'sw', 'w', 'nw', 'ne']
    index = 0
    while index < len(line):
        for d in dirs:
            if line[index:].find(d) == 0:
                moves.append(d)
                index += len(d)
                break
    dx,dy = coord_from_moves(moves)
    coords = coord_str(dx,dy)
    if coords in seen:
        seen[coords] += 1
    else:
        seen[coords] = 1

def hexbystr(hex, coords):
    if coords in hex:
        return hex[coords] % 2
    else:
        return 0

def hexbycoords(hex, x, y):
    coords = coord_str(x,y)
    return hexbystr(hex,coords)

def coord_str(x,y):
    return str(x)+','+str(y)

def test_coord(hex, x, y):
    neighbors = [coord_str(x+1, y),  coord_str(x+1, y-1), coord_str(x, y-1), coord_str(x-1, y), coord_str(x-1, y+1), coord_str(x, y+1)]
    neighbor_sum = 0
    for n in neighbors:
        if(hexbystr(hex, n) == 1):
            neighbor_sum += 1
    local_val = hexbycoords(hex,x,y)
    if local_val == 1 and (neighbor_sum == 0 or neighbor_sum > 2):
        return 0
    elif local_val == 0 and neighbor_sum == 2:
        return 1
    else:
        return local_val
    
def count(hex):
    count = 0
    min_x,max_x, min_y,max_y = hex_bounds(hex)
    for coord in hex:
        if hexbystr(hex,coord) == 1:
            count += 1
    return count
    
def advance_day(hexA, hexB):
    min_x,max_x, min_y,max_y = hex_bounds(hexA)
    hexB.clear()
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            coords = coord_str(x,y)
            if(test_coord(hexA,x,y) == 1):
                hexB[coords] = 1
    
def day24(infile):
    f = open(infile, 'r')
    lines = f.read().splitlines()
    
    seen = {}
    for line in lines:
        follow_line(line, seen)
    
    part1 = 0
    for s in seen:
        if seen[s] % 2 == 1:
            part1+=1
    print("Part 1: %d" % part1)
    
    hexA = seen.copy()
    hexB = {}
    for d in range(0, 100):
        if d % 2 == 0:
            advance_day(hexA, hexB)
        else:
            advance_day(hexB, hexA)
    part2 = count(hexA)
    print("Part 2: %d" % part2)
    