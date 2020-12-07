#day1.py

def day1(infile):
    f = open(infile, 'r')
    lines = f.readlines()
    entries = []
    for line in lines:
        entry = int(line)
        entries.append(entry)
    
    found = False
    for i in range(len(entries)):
        if found:
            break
        for j in range(i+1, len(entries)):
            if found:
                break
            if(entries[i] + entries[j] == 2020):
                print("Part 1: %d" % (entries[i]*entries[j]))
                found = True
                break
    
    found = False
    for i in range(len(entries)):
        if found:
            break
        for j in range(i+1, len(entries)):
            if found:
                break
            for k in range(j+1, len(entries)):
                if(entries[i] + entries[j] + entries[k] == 2020):
                    print("Part 2: %d" % (entries[i]*entries[j]*entries[k]))
                    found = True
                    break
    