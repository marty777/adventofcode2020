#day23.py

class SLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class SLList:
    def __init__(self):
        self.start = None
        self.len = 0
        self.maxval = 9
    def setmax(self, maxval):
        self.maxval = maxval    
    def append(self, val):
        if self.start == None:
            node = SLNode(val)
            self.start = node
            self.len = 1
            if(val > self.maxval):
                self.maxval = val
            return node
        else:
            if self.len == 1:
                node = SLNode(val)
                node.prev = self.start
                node.next = self.start
                self.start.next = node
                self.start.prev = node
                self.len += 1
                return node
            else:
                node = SLNode(val)
                start_node = self.start
                prev_node = self.start.prev
                node.prev = prev_node
                node.next = start_node
                start_node.prev = node
                prev_node.next = node
                self.len += 1
                return node
    def insert(self, val, after_val):
        index_node = self.start
        for i in range(0, self.len):
            if index_node.val == after_val:
                break
            index_node = index_node.next
        next_node = index_node.next
        node = SLNode(val)
        index_node.next = node
        next_node.prev = node
        node.next = next_node
        node.prev = index_node
        self.len += 1
    def pop_after_start(self):
        node = self.start.next
        node.next.prev = self.start
        self.start.next = node.next
        self.len -= 1
        return node.val
    def in_list(self, val):
        node = self.start
        for i in range(0,self.len):
            if node.val == val:
                return True
            node = node.next
        return False
    def findnodebyval(self,val):
        node = self.start
        while(node.val != val):
            node = node.next
        return node
    def liststr(self, mode):
        if self.len == 0:
            return '[]'
        else:
            if mode == 0:
                node = self.start
                ret = '('+str(node.val)+')'
                for i in range(1, self.len):
                    node = node.next
                    ret += ' '+str(node.val)
                return ret
            else:
                node = self.start
                while node.val != 1:
                    node = node.next
                ret = ''
                for i in range(0, self.len - 1):
                    node = node.next
                    ret += str(node.val)
                return ret

def move(cuplist, direct_index):
    popcups = []
    popcups.append(cuplist.pop_after_start())
    popcups.append(cuplist.pop_after_start())
    popcups.append(cuplist.pop_after_start())
   
    dest_val = cuplist.start.val - 1
    if(dest_val < 1):
        dest_val = cuplist.maxval
    while True:
        found = False
        for c in popcups:
            if dest_val == c:
                dest_val -= 1
                if(dest_val < 1):
                    dest_val = cuplist.maxval
                found = True
        if not found:
            break
    dest_node = None
    if dest_val in direct_index:
        dest_node = direct_index[dest_val]
       
    next_node = dest_node.next
    dest_node.next = SLNode(popcups[0])
    dest_node.next.prev = dest_node
    dest_node.next.next = SLNode(popcups[1])
    dest_node.next.next.prev = dest_node.next
    dest_node.next.next.next = SLNode(popcups[2])
    dest_node.next.next.next.prev = dest_node.next.next
    dest_node.next.next.next.next = next_node
    
    direct_index[popcups[0]] = dest_node.next
    direct_index[popcups[1]] = dest_node.next.next
    direct_index[popcups[2]] = dest_node.next.next.next
    
    cuplist.len += 3
    
    cuplist.start = cuplist.start.next

def day23(infile):
    f = open(infile, 'r')
    lines = f.read().splitlines()
    cups = []
    
    print("This may take a while...")
    
    cupstr = lines[0]
    for i in range(0, len(cupstr)):
        cups.append(int(cupstr[i]))
    
    direct_index = {}
    cuplist = SLList()
    cuplist.maxval = 9
    for c in cups:
        direct_index[c] = cuplist.append(c)
    
    for i in range(0, 100):
        move(cuplist, direct_index)
    part1 = cuplist.liststr(1)
    print("Part 1: %s" % part1)
    
    cuplist = SLList()
    cupmax = 0
    direct_index = {}
    for c in cups:
        direct_index[c] = cuplist.append(c)
        if c > cupmax:
            cupmax = c
            
    index = cupmax + 1
    while index <= 1000000:
        direct_index[index] = cuplist.append(index)
        index += 1
    cuplist.setmax(1000000)
    one_node = cuplist.findnodebyval(1)
    for i in range(0, 10000000):
        move(cuplist, direct_index)
    node = cuplist.start
    steps = 0
    while(node.val != 1):
        node = node.next
        steps += 1
    print("Part 2: %d" % (node.next.val * node.next.next.val))