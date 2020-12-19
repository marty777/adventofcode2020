#day19.py
#second attempt with regexes

import re

def generate_regex(rules, rule_index, depth, max_depth ):
    if depth > max_depth:
        return ''
    if(rules[rule_index].find('"') > -1):
        return rules[rule_index][1]
    current_rules = []
    for group in rules[rule_index].split('|'):
        inner_regex = []
        for inner_rule in group.split():
            inner_regex.append(generate_regex(rules, inner_rule, depth+1, max_depth))
        current_rules.append("".join(inner_regex))
    return '(' + '|'.join(current_rules) + ')'

def day19(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    rules = {}
    messages = []
    
    i = 0
    sum = 0
    block = 0
    maxlen = 0
    for line in lines:
        if(line == '\n'):
            block += 1
            continue
        if(block == 0):
            if line[-1] == '\n':
                line = line[:-1]
            rules[line.split(': ')[0]] = line.split(": ")[1]
        else:
            if(line[-1] == '\n'):
                line = line[:-1]
            messages.append(line)
            if(len(line) > maxlen):
                maxlen = len(line)
    
    # using maxlen, length of largest message, as heuristic to limit
    # depth of search
    regex = re.compile(generate_regex(rules, '0', 0, maxlen//4))
    matches = 0
    for m in messages:
        if(regex.fullmatch(m)):
            matches+=1
    print("Part 1: %d" % matches)
    
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'
    regex2 = re.compile(generate_regex(rules, '0', 0, maxlen//4))
    matches = 0
    for m in messages:
        if(regex2.fullmatch(m)):
            matches+=1
    print("Part 2: %d" % matches)