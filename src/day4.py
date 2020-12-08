#day4.py

class PassportData:
    def __init__(self):
        self.dict = {}
        
    def addline(self, line):
        line2 = line[0:-1] #omit newline
        sections = line2.split(' ')
        for section in sections:
            fieldval = section.split(':')
            self.dict[fieldval[0]] = fieldval[1]
    def is_valid_1(self):
        required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']        
        for req in required:
            if (req not in self.dict):
                return False
        return True
    def is_valid_2(self):
        required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        #byr
        if ('byr' not in self.dict):
            return False
        byr = int(self.dict['byr'])
        if byr < 1920 or byr > 2002:
            return False
        #iyr
        if ('iyr' not in self.dict):
            return False
        iyr = int(self.dict['iyr'])
        if iyr < 2010 or iyr > 2020:
            return False
        #eyr
        if ('eyr' not in self.dict):
            return False
        eyr = int(self.dict['eyr'])
        if eyr < 2020 or eyr > 2030:
            return False
        #hgt
        if ('hgt' not in self.dict):
            return False
        
        if(len(self.dict['hgt']) < 3 or (self.dict['hgt'][-2:] != 'in' and self.dict['hgt'][-2:] != 'cm')):
            return False
        hgt = int(self.dict['hgt'][0:-2])
        if(self.dict['hgt'][-2:] == 'cm' and (hgt < 150 or hgt > 193)):
            return False
        if(self.dict['hgt'][-2:] == 'in' and (hgt < 59 or hgt > 76)):
            return False
        #hcl
        if ('hcl' not in self.dict):
            return False
        hcl = self.dict['hcl']
        hcl_valid = '0123456789abcdef'
        if(len(hcl) != 7 or hcl[0] != '#'):
            return False
        for i in range(1,7):
            if(hcl_valid.find(hcl[i]) == -1):
                return False
        #ecl
        if ('ecl' not in self.dict):
            return False
        ecl = self.dict['ecl']
        ecl_valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if(ecl not in ecl_valid):
            return False
        #pid 
        if ('pid' not in self.dict):
            return False
        pid_valid = '0123456789'
        pid = self.dict['pid']
        if(len(pid) != 9):
            return False
        for i in range(0,9):
            if pid_valid.find(pid[i]) == -1:
                return False
        return True
    
    

def day4(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    entries = [];
    entries.append(PassportData())
    valid_passwords1 = 0
    valid_passwords2 = 0
    for line in lines:
        if line == '\n':
            entries.append(PassportData()) # new passport
            continue
        entries[len(entries) - 1].addline(line)
    
    valid1 = 0
    valid2 = 0
    for entry in entries:
        if entry.is_valid_1():
            valid1 += 1
        if entry.is_valid_2():
            valid2 += 1
        #entry.is_valid_2()
        #entry.printself()
    # entries[0].dict['eyr'] = '2020'
    # entries[0].dict['hgt'] = '189cm'
    # entries[0].dict['hcl'] = '#123abc'
    # entries[0].dict['ecl'] = 'oth'
    # entries[0].dict['pid'] = '00000000a'
    # entries[0].is_valid_2()
    
    print("Part 1: %d" % valid1)
    print("Part 2: %d" % valid2)
        
    
    
    