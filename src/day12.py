#day12.py

class Nav:
    def __init__(self,line):
        if line[len(line)-1] == '\n':
            line = line[:-1]
        self.cmd = line[0:1]
        self.val = int(line[1:])
        
class Ferry:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 1
        self.dirs = ['N','E','S','W']
        self.w_x = 10
        self.w_y = 1
    def move(self, cmd, val):
        if cmd == 'N':
            self.y += val
        elif cmd == 'E':
            self.x += val
        elif cmd == 'S':
            self.y -= val
        elif cmd == 'W':
            self.x -= val
        elif cmd == 'R':
            inc = int(val/90)
            self.dir = (self.dir + inc) % 4
        elif cmd == 'L':
            inc = int(val/90)
            self.dir = (self.dir + 4 - inc) % 4
        elif cmd == 'F':
            if self.dir == 0:
                self.y += val
            elif self.dir == 1:
                self.x += val
            elif self.dir == 2:
                self.y -= val
            elif self.dir == 3:
                self.x -= val
                
    def move2(self, cmd, val):
        if cmd == 'N':
            self.w_y += val
        elif cmd == 'E':
            self.w_x += val
        elif cmd == 'S':
            self.w_y -= val
        elif cmd == 'W':
            self.w_x -= val
        elif cmd == 'R':
            inc = int(val/90)
            for i in range(0,inc):
                start_y = self.w_y
                start_x = self.w_x
                self.w_y = self.w_x * -1
                self.w_x = start_y
            self.dir = (self.dir + inc) % 4
        elif cmd == 'L':
            inc = int(val/90)
            for i in range(0,inc):
                start_y = self.w_y
                
                self.w_y = self.w_x
                self.w_x = start_y * -1
        elif cmd == 'F':
            self.x += self.w_x * val
            self.y += self.w_y * val
                
def day12(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    entries = []
    
    ferry = Ferry()
    
    for i in range(0,len(lines)):
        line = lines[i]
        entries.append(Nav(line))
        
    for nav in entries:
        ferry.move(nav.cmd, nav.val)
    print("Part 1: %d" % (abs(ferry.x) + abs(ferry.y)))
    
    ferry2 = Ferry()
    for nav in entries:
        ferry2.move2(nav.cmd, nav.val)
    
    print("Part 2: %d" % (abs(ferry2.x) + abs(ferry2.y)))
    