#day5.py

rows = 128
seats_per_row = 8

class BoardingpassData:
    def __init__(self, line):
        self.txt = line[0:10] #omit newline
    def seatindex(self):
        min_row = 0
        max_row = rows - 1
        for i in range(0,7):
            if self.txt[i] == 'B':
                min_row = min_row + ((max_row - min_row + 1) / 2)
            else:
                max_row = max_row - ((max_row - min_row + 1 ) / 2)
        min_seat = 0
        max_seat = seats_per_row - 1
        for i in range(7,10):
            if(self.txt[i] == 'R'):
                min_seat = min_seat + ((max_seat - min_seat + 1) / 2)
            else:
                max_seat = max_seat - ((max_seat - min_seat + 1) / 2)
        return int((seats_per_row*min_row) + min_seat)

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
    test = BoardingpassData('FBFBBFFRLR')
    indexes = [];
    for i in range(0,rows*seats_per_row):
        indexes.append(False)
    for entry in entries:
        indexes[entry.seatindex()] = True
    
    for i in range(1, len(indexes) - 1):
        if not indexes[i] and indexes[i-1] and indexes[i+1]:
            print("Part 2: %d" % (i)) 
            break
    
    
    