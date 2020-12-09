#day6.py

num_questions = 26

class AnswerData:
    def __init__(self):
        self.answers1 = [False] * num_questions
        self.answers2 = [True] * num_questions
        self.groupsize = 0
    def addline(self, line):
        answers = line[0:-1] #omit newline
        answers2 = [False] * num_questions
        self.groupsize += 1
        for a in answers:
            val = ord(a) - 97
            self.answers1[val] = True
            answers2[val] = True
        # logical AND each row
        for i in range(0,num_questions): 
            self.answers2[i] &= answers2[i]
        
    def count_answers1(self):
        count = 0
        for answer in self.answers1:
            if answer:
                count += 1
        return count
    def count_answers2(self):
        count = 0
        for answer in self.answers2:
            if answer:
                count += 1
        return count

def day6(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    entries = [];
    entries.append(AnswerData())
    valid_passwords1 = 0
    valid_passwords2 = 0
    for line in lines:
        if line == '\n':
            entries.append(AnswerData()) # new passport
            continue
        entries[len(entries) - 1].addline(line)
    
    answered_count1 = 0
    answered_count2 = 0
    for entry in entries:
        answered_count1 += entry.count_answers1()
        answered_count2 += entry.count_answers2()
    
    print("Part 1: %d" % answered_count1)
    print("Part 2: %d" % answered_count2)
