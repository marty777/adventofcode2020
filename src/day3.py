#day3.py

def day3(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    hill = []
    line_num = 0;
    for i in range(0, len(lines)):
        hill.append([])
        for j in range(0, len(lines[i]) - 1): #skip linebreak
            hill[i].append(bool(lines[i][j] == '#'))
            
    tree_count = evaluate_hill(hill, 3, 1)
    print("Part 1: %d" % tree_count)
    a = evaluate_hill(hill, 1, 1)
    b = evaluate_hill(hill, 3, 1)
    c = evaluate_hill(hill, 5, 1)
    d = evaluate_hill(hill, 7, 1)
    e = evaluate_hill(hill, 1, 2)
    print("Part 2: %d" % (a*b*c*d*e))
    
def evaluate_hill(hill, dx, dy):
    y = 0
    x = 0
    count = 0
    while y < len(hill) - 1:
        if hill[y][x]:
            count += 1
        x = (x + dx) % len(hill[0])
        y = y + dy
    return count