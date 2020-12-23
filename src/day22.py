#day22.py

def handstr(deck1, deck2):
    one = ",".join(str(d) for d in deck1)
    two = ",".join(str(d) for d in deck2)
    return '['+one+'][' +two+ ']'

def game2(deck1, deck2, depth):
    winner = 0
    cache = {}
    round = 1
    while(len(deck1) > 0 and len(deck2) > 0):
        cache_str = handstr(deck1, deck2)
        if cache_str in cache:
            winner = 1
            break
        cache[cache_str] = True
        
        top1 = deck1.pop(0)
        top2 = deck2.pop(0)
        if top1 <= len(deck1) and top2 <= len(deck2):
            deck1_copy = deck1.copy()
            deck2_copy = deck2.copy()
            winner_recurse = game2(deck1_copy[0:top1], deck2_copy[0:top2], depth + 1)
            if(winner_recurse == 1):
                deck1.append(top1)
                deck1.append(top2)
            else:
                deck2.append(top2)
                deck2.append(top1)
        else:
            if(top1 > top2):
                deck1.append(top1)
                deck1.append(top2)
            else:
                deck2.append(top2)
                deck2.append(top1)
        round += 1
    if(winner > 0):
        return winner
    else:
        if(len(deck1) > len(deck2)):
            return 1
        else:
            return 2

def game1(deck1, deck2):
    while(len(deck1) > 0 and len(deck2) > 0):
        top1 = deck1.pop(0)
        top2 = deck2.pop(0)
       
        if(top1 > top2):
            deck1.append(top1)
            deck1.append(top2)
        else:
            deck2.append(top2)
            deck2.append(top1)

def score(deck1, deck2):
    sum = 0
    if len(deck1) > len(deck2):
        for i in range(0, len(deck1)):
            sum += (len(deck1) - i) * deck1[i]
    else:
        for i in range(0, len(deck2)):
            sum += (len(deck2) - i) * deck2[i]
    return sum

def day22(infile):
    f = open(infile, 'r')
    lines = f.read().splitlines()
    foods = []
    
    curr_player = 1
    deck1 = []
    deck2 = []
    for line in lines:
        if len(line) ==  0:
            continue
        if line.find("Player 1:") != -1:
            curr_player = 1
            continue
        elif line.find("Player 2:") != -1:
            curr_player = 2
            continue
        if curr_player == 1:
            deck1.append(int(line))
        else:
            deck2.append(int(line))
    
    deck1_backup = deck1.copy()
    deck2_backup = deck2.copy()
    
    game1(deck1, deck2)
    sum = score(deck1, deck2)
    print("Part 1: %s" % sum)
    
    deck1 = deck1_backup.copy()
    deck2 = deck2_backup.copy()
    
    game2(deck1,deck2, 0)    
    sum = score(deck1, deck2)
    print("Part 2: %s" % sum)
