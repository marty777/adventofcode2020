#day7.py

rows = 128
seats_per_row = 8

class BagCapacity:
    def __init__(self, num, tag):
        self.num = num
        self.tag = tag
class BagData:
    def __init__(self, line):
        self.txt = line[0:-1] #omit newline
        tag_split = self.txt.split(' bags contain ')
        self.tag = tag_split[0].replace(' ', '')
        
        self.contains = []
        if(tag_split[1].find('no other bags') != -1):
            return
        content_split = tag_split[1].split(', ')
        for content in content_split:
            term_split = content.split(' ')
            tag = ''
            count = 0
            for term in term_split:
                if(term.isnumeric()):
                    count = int(term)
                    continue
                if(term[0:3] == 'bag'):
                    break
                tag += term
            self.contains.append(BagCapacity(count, tag))
    def contains_tag(self, tag):
        for content in self.contains:
            if(content.tag == tag):
                return True
        return False
        
def search_entries(entries, tag):
    for i in range(0,len(entries)):
        if entries[i].tag == tag:
            return i
    return -1
    
def recurse(entries,tag):
    count = 0
    bagdata_index = search_entries(entries,tag)
    bagdata = entries[bagdata_index]
    for bag in bagdata.contains:
        count += bag.num * (recurse(entries, bag.tag) + 1)
    return count
    
def day7(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    entries = [];
    max_index = 0
    part1 = {}
    for line in lines:
        entries.append(BagData(line))
    
    # initial containment
    for entry in entries:
        if entry.contains_tag('shinygold'):
            part1[entry.tag] = True
    count = len(part1)
    last_count = count

    done = False
    while not done:
        keys = list(part1.keys())
        for key in keys:
            index = search_entries(entries, key)
            if(index == -1):
                continue
            # add all tags that can contain the current tag
            for bag in entries:
                if bag.contains_tag(key):
                    if(bag.tag not in keys):
                        part1[(bag.tag)] = True
                        keys.append(bag.tag)
        count = len(part1)
        if(count == last_count):
            done = True
        last_count = count
        
    print("Part 1: %d" % len(part1))
    part2 = recurse(entries, 'shinygold')
    print("Part 2: %d" % part2)
    
    
    
    