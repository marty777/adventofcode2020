#day16.py

class TicketRule:
    def __init__(self, line):
        self.name = line[0:line.find(":")]
        range = line[line.find(":")+2:]
        ranges = range.split(" or ")
        low_a, high_a = ranges[0].split("-")
        self.low_a = int(low_a)
        self.high_a = int(high_a)
        low_b, high_b = ranges[1].split("-")
        self.low_b = int(low_b)
        self.high_b = int(high_b)
    def test2(self, tickets, assignments):
        valid_indexes = []
        for i in range(0, len(tickets[0].vals)):
            previously_found = False
            for k in assignments:
                if assignments[k] == i:
                    previously_found = True
                    break
            if previously_found:
                continue
            valid = True
            for ticket in tickets:
                val = ticket.vals[i]
                if not ((val >= self.low_a and val <= self.high_a) or (val >= self.low_b and val <= self.high_b)):
                    valid = False
                    break
            if valid:
                valid_indexes.append(i)
        return valid_indexes
class Ticket:
    def __init__(self, line):
        self.vals = []
        split = line.split(',')
        for s in split:
            self.vals.append(int(s))
    # reddit points out that a ticket with a zero field that doesn't match any rules 
    # would cause issues if checking for valid tickets using the sum of invalid fields. 
    # hence the two return values
    # note that this did get me, although it didn't prevent me from finding the solution 
    # to part 2. while i failed to filter out one invalid ticket, it didn't prevent me 
    # from finding all departure fields. it did stop me from finding a solution that matched 
    # up all fields.
    def test1(self, rules):
        invalid_sum = 0
        invalid = False
        for val in self.vals:
            valid = False
            for rule in rules:
                if (val >= rule.low_a and val <= rule.high_a) or (val >= rule.low_b and val <= rule.high_b):
                    valid = True
                    break
            if not valid:
                invalid_sum += val
                invalid = True
        return invalid_sum, invalid
        
def day16(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    rules = []
    tickets = []
    real_tickets = []
    
    mode = 0
    i = 0
    for line in lines:
        i+=1
        if line == '\n':
            mode += 1
            continue
        if(mode == 0):
            rules.append(TicketRule(line))
        elif(mode == 2):
            if(line == 'nearby tickets:\n'):
                continue
            tickets.append(Ticket(line))
        else:
            if(line == 'your ticket:\n'):
                continue
            my_ticket = Ticket(line)
    
    invalid_sum = 0
    for ticket in tickets:
        invalid_count, invalid = ticket.test1(rules)
        if(not invalid):
            real_tickets.append(ticket)
        invalid_sum += invalid_count
    print("Part 1: %d" % invalid_sum)
    
    departure_str = "departure"
    
    done = False
    remaining = len(rules)
    assignments = {}
    while not done:
        for i in range(0, len(rules)):
            if i in assignments:
                continue
            candidates = rules[i].test2(real_tickets, assignments)
            if len(candidates) == 1:
                assignments[i] = candidates[0]
                remaining -= 1
            if(remaining == 0):
                break
        curr_departures = 0
        if(remaining == 0):
            done = True
    
    product = 1
    for i in range(0, len(rules)):
        if(rules[i].name.find(departure_str) != -1):
            product *= my_ticket.vals[assignments[i]]
    print("Part 2: %d" % product)