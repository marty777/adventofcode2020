#day2.py

import sys

class PasswordLine:
    def __init__(self, minstr, maxstr, letter, password):
        try:
            self.min= int(minstr)
            self.max = int(maxstr)
            self.letter = letter
            self.password = password
        except:
            sys.exit('An error occured while parsing the input file')
    def evaluate1(self):
        count = self.password.count(self.letter)
        if count < self.min or count > self.max:
            return False
        return True
    def evaluate2(self):
        count = self.password.count(self.letter)
        if bool(self.password[self.min - 1] == self.letter) ^ bool(self.password[self.max - 1] == self.letter):
            return True
        return False

def day2(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    entries = []
    valid_passwords1 = 0
    valid_passwords2 = 0
    for line in lines:
        pos = 0
        minstr = line[0:line.find('-')]
        pos = len(minstr)
        maxstr = line[(pos+1):line.find(' ', pos)]
        pos += 1 + len(maxstr)
        letter = line[(pos+1):line.find(':', pos)]
        pos += 2 + len(letter)
        password = line[pos+1:-1] #omit ending linebreak
        entry = PasswordLine(minstr, maxstr, letter, password)
        if entry.evaluate1():
            valid_passwords1 += 1
        if entry.evaluate2():
            valid_passwords2 += 1
        entries.append(entry)
    print("Part 1: %d" % valid_passwords1)
    print("Part 2: %d" % valid_passwords2)
    
    