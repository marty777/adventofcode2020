#day5.py

rows = 128
seats_per_row = 8

class BoardingpassData:
    def __init__(self, line):
        self.txt = line[0:10] #omit newline
    def seatindex(self):
        min_row = 0
        max_row = rows - 1
        index = 0
        for i in range(0,10):
            if self.txt[i] == 'B' or self.txt[i] == 'R':
                index |= 1 << (9 - i)
        return index

def day5(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    entries = [];
    max_index = 0
    for line in lines:
        entries.append(BoardingpassData(line))
        index = entries[len(entries) - 1].seatindex()
        if index > max_index:
            max_index = index
    print("Part 1: %d" % (max_index))
    indexes = [];
    for i in range(0,rows*seats_per_row):
        indexes.append(False)
    for entry in entries:
        indexes[entry.seatindex()] = True
    
    for i in range(1, len(indexes) - 1):
        if not indexes[i] and indexes[i-1] and indexes[i+1]:
            print("Part 2: %d" % (i)) 
            break
    
    
    