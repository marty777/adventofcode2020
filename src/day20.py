#day20.py
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class TilePos:
    def __init__(self, x, y, rotation, reflect_x, reflect_y):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.reflect_x = reflect_x
        self.reflect_y = reflect_y
    def posstr(self):
        return "X:" + str(self.x) + " Y:" +  str(self.y) + " R:" +  str(self.rotation) + " RX:" +  str(self.reflect_x) +" RY:" +  str(self.reflect_y)
    
class MapTile:
    def __init__(self, lines):
        for i in range(0,len(lines)):
            if lines[i][-1] == '\n':
                lines[i] = lines[i][:-1]
        id = lines[0]
        id = id.replace('Tile ', '')
        id = id.replace(':', '')
        self.id = int(id)
        self.grid = []
        for i in range(1,len(lines)):
            if lines[i] == '\n' or len(lines[i]) == 0:
                continue
            self.grid.append([])
            for j in range(0, len(lines[i])):
                if(lines[i][j] == '#'):
                    self.grid[i-1].append(True)
                elif(lines[i][j] == '.'):
                    self.grid[i-1].append(False)
        
    def width(self):
        return len(self.grid[0])
    def height(self):
        return len(self.grid)
    def transform_coord(self, x, y, rotations, reflect_x, reflect_y):
        curr_x = x
        curr_y = y
        if reflect_x:
            curr_x = self.width() - 1 - curr_x
        if reflect_y:
            curr_y = self.height() - 1 - curr_y
        # rotations is number of 90 degree rotations counterclockwise
        for i in range(0, rotations):
            new_x = self.height() - 1 - curr_y
            new_y = curr_x
            curr_x = new_x
            curr_y = new_y
        return curr_x, curr_y
        
    def printmap(self, rotations, reflect_x, reflect_y):
        print("Tile ", self.id, ":")
        for i in range(0, self.height()):
            for j in range(0, self.width()):
                coord_x, coord_y = self.transform_coord(j,i,rotations,reflect_x,reflect_y)
                if(self.grid[coord_y][coord_x]):
                    print('#', end='')
                else:
                    print('.', end='')
            print('')
    # returns number of possible matching configurations with neighbor
    # if only one possible, returns the rotation and reflection for the neigbor
    def test_neighbor(self, tile, dir, self_transformation):
        src = self.get_edge(dir, self_transformation.rotation, self_transformation.reflect_x, self_transformation.reflect_y)
        dest_dir = opposite_dir(dir)
        neigbor_x, neighbor_y = neighbor_pos(self_transformation.x, self_transformation.y, dir)
        matches = []
        for i in range(0, 4):
            for j in range(0,2):
                # reflection in both x and y is equivalent to 180 degree rotation. Skip it
                # 180 degree rotation + x reflection + y reflection ~= no transformation
                match = True
                dst = tile.get_edge(dest_dir, i, (j == 1), False)
                for l in range(0, len(src)):
                    if dst[l] != src[l]:
                        match = False
                        break
                if match:
                    matches.append(TilePos(neigbor_x, neighbor_y, i,  (j == 1), False))               
        if len(matches) == 1:
            return 1, matches[0].rotation, matches[0].reflect_x, matches[0].reflect_y
        else:
            return len(matches), 0, False, False
        
    def get_edge(self, dir, rotations, reflect_x, reflect_y):
        ret = []
        if dir == NORTH:
            for i in range(0, self.width()):
                transform_x, transform_y = self.transform_coord(i, 0, rotations, reflect_x, reflect_y)
                ret.append(self.grid[transform_y][transform_x])
        elif dir == EAST:
            for i in range(0, self.height()):
                transform_x, transform_y = self.transform_coord(self.width() -  1, i, rotations, reflect_x, reflect_y)
                ret.append(self.grid[transform_y][transform_x])
        elif dir == SOUTH:
            for i in range(0, self.width()):
                transform_x, transform_y = self.transform_coord(i, self.height() - 1, rotations, reflect_x, reflect_y)
                ret.append(self.grid[transform_y][transform_x])
        elif dir == WEST:
            for i in range(0, self.height()):
                transform_x, transform_y = self.transform_coord(0, i, rotations, reflect_x, reflect_y)
                ret.append(self.grid[transform_y][transform_x])
        return ret

# returns SOUTH if NORTH, EAST if WEST, etc
def opposite_dir(dir):
    return (dir + 2) % 4
    
def neighbor_pos(src_x,src_y,dest_dir):
    if dest_dir == NORTH:
        return src_x, src_y+1
    elif dest_dir == EAST:
        return src_x + 1, src_y
    elif dest_dir == SOUTH:
        return src_x, src_y - 1
    elif dest_dir == WEST:
        return src_x - 1, src_y

def solve_layout(maps):
    # for each tile, determine a position, rotation and reflection in x and y
    # such that we have a single solution for all tiles (equivalent under rotation/reflection)
    
    # pick a fixed orientation for one tile and build others around it
    fixed = {}
    fixed[0] = TilePos(0,0, 0, False, False) # no transformation, fix position at 0, 0 for tile 0
    while len(fixed) < len(maps):
        for i in range(0, len(maps)):
            # test up, down, left, right for all other tiles under
            # all other reflections and rotations
            # ideally there will only be one solution for one of those
            # directions. If so, fix that tile in that position and repeat
            if i in fixed:
                set = [False] * 4
                for j in fixed:
                    if j == i:
                        continue
                    if fixed[j].x == fixed[i].x and fixed[j].y == fixed[i].y + 1:
                        set[NORTH] = True
                    elif fixed[j].x == fixed[i].x + 1 and fixed[j].y == fixed[i].y:
                        set[EAST] = True
                    elif fixed[j].x == fixed[i].x and fixed[j].y == fixed[i].y - 1:
                        set[SOUTH] = True
                    elif fixed[j].x == fixed[i].x - 1 and fixed[j].y == fixed[i].y:
                        set[WEST] = True
                        
                for dir in range(0,4):
                    if not set[dir]:
                        for k in range(0, len(maps)):
                            if k not in fixed:
                                match_count, rot, ref_x, ref_y = maps[i].test_neighbor(maps[k], dir, fixed[i])
                                if(match_count == 1):
                                    new_x, new_y = neighbor_pos(fixed[i].x, fixed[i].y, dir)
                                    fixed[k] = TilePos(new_x, new_y, rot, ref_x, ref_y)
        
    max_x, min_x, max_y, min_y = tile_position_bounds(fixed)
    corner_tl = 0
    corner_tr = 0
    corner_br = 0
    corner_bl = 0
    for i in fixed:
        if fixed[i].x == min_x and fixed[i].y == max_y:
            corner_tl = maps[i].id
        elif fixed[i].x == max_x and fixed[i].y == max_y:
            corner_tr = maps[i].id
        elif fixed[i].x == max_x and fixed[i].y == min_y:
            corner_br = maps[i].id
        elif fixed[i].x == min_x and fixed[i].y == min_y:
            corner_bl = maps[i].id
    part1 = corner_tl*corner_tr*corner_br*corner_bl
    return part1, fixed

def monster_scan(map, rotation, reflect_x): 
    monsterlines = []
    monsterlines.append('                  # ')
    monsterlines.append('#    ##    ##    ###')
    monsterlines.append(' #  #  #  #  #  #   ')
    monster = []
    monster_pixels = 0
    matches = 0
    rough_waters = 0
    for i in range(0, map.height()):
        for j in range(0, map.width()):
            if map.grid[j][i]:
                rough_waters += 1
    for i in range(0, len(monsterlines)):
        monster.append([False] * len(monsterlines[i]))
        for j in range(0, len(monsterlines[i])):
            if monsterlines[i][j] == '#':
                monster[i][j] = True
                monster_pixels += 1
    
    # not transforming dimensions, better hope width and height are identical
    for i in range(0, map.height() - len(monster)):
        for j in range(0, map.width() - len(monster[0])):           
            matched_pixels = 0
            for m_y in range(0, len(monster)):
                for m_x in range(0, len(monster[m_y])):
                    image_x, image_y = map.transform_coord(j+m_x, i+m_y, rotation, reflect_x, False)
                    if monster[m_y][m_x] and map.grid[image_y][image_x]:
                        matched_pixels += 1
            if matched_pixels == monster_pixels:
                matches += 1
    if matches > 0:
        # assuming no monsters overlap
        return (rough_waters - (monster_pixels * matches))
    else:
        return 0

def tile_position_bounds(positions):
    max_x = min_x = max_y = min_y = 0
    for i in positions:
        if positions[i].x < min_x:
            min_x = positions[i].x
        if positions[i].x > max_x:
            max_x = positions[i].x
        if positions[i].y < min_y:
            min_y = positions[i].y
        if positions[i].y > max_y:
            max_y = positions[i].y
    return max_x, min_x, max_y, min_y
    
def extract_image(maps, positions):
    image = []
    max_x, min_x, max_y, min_y = tile_position_bounds(positions)
            
    imagewidth = ((max_x - min_x + 1) * (maps[0].width() - 2))
    imageheight = ((max_y - min_y + 1) * (maps[0].height() - 2))
    for i in range(0, imageheight):
        image.append([False] * imagewidth)
    
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            index = -1
            for i in positions:
                if positions[i].x == x and positions[i].y == y:
                    index = i
                    break
            for y1 in range(1, maps[index].height() - 1):
                for x1 in range(1, maps[index].width() - 1):
                    transform_x, transform_y = maps[index].transform_coord(x1, y1, positions[index].rotation, positions[index].reflect_x, positions[index].reflect_y)
                    image_coord_x = (x - min_x) * (maps[index].width() - 2) + (x1 - 1)
                    image_coord_y = (max_y - y) * (maps[index].height() - 2) + (y1 - 1)
                    image[image_coord_y][image_coord_x] = maps[index].grid[transform_y][transform_x]
    imagelines = []
    imagelines.append('Tile 1:')
    for i in range(0, imageheight):
        line = ''
        for j in range(0, imagewidth):
            if(image[i][j]):
                line += '#'
            else:
                line += '.'
        imagelines.append(line)
    bigmap = MapTile(imagelines)
    return bigmap
    
def loadmaps(lines, maps):
    last_index = 0
    for i in range(0, len(lines)):
        if lines[i] == '\n' or i == len(lines) - 1:
            if i == len(lines) - 1:
                maps.append(MapTile(lines[last_index:i+1]))
            else:
                maps.append(MapTile(lines[last_index:i]))
            last_index = i+1

def day20(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    maps = []
    
    loadmaps(lines, maps)
    part1, positions = solve_layout(maps)
    print("Part 1: %d" % part1)
    image = extract_image(maps, positions)
    for i in range(0,4): # rotations
        for j in range(0,2): # reflection
            result = monster_scan(image, i, j==1)
            if result > 0:
                print("Part 2: %d" % result)
                return