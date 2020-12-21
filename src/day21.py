#day21.py

class Food:
    def __init__(self, line):
        self.ingredients = {}
        self.allergens = {}
        splitA = line.split(" (contains ")
        allergen_str = splitA[1]
        allergen_str = allergen_str[:-1] # closing bracket
        allergens = allergen_str.split(", ")
        for a in allergens:
            self.allergens[a] = True
        ingredient_str = splitA[0]
        ingredients = ingredient_str.split(" ")
        for i in ingredients:
            self.ingredients[i] = True


def day21(infile):
    f = open(infile, 'r')
    lines = f.read().splitlines()
    foods = []
    
    for line in lines:
        foods.append(Food(line))
        
    # part 1: list all foods that do not appear in every instance of an allergen
    candidates = {}
    allergen_counts = {}
    ingredients_count = {}
    for f in foods:
        for i in f.ingredients:
            candidates[i] = True
            if i in ingredients_count:
                ingredients_count[i] += 1
            else:
                ingredients_count[i] = 1
        for a in f.allergens:
            if a in allergen_counts:
                allergen_counts[a] += 1
            else:
                allergen_counts[a] = 1
    
    candidates_part1 = candidates.copy()
    for c in candidates:
        a_count = {}
        for f in foods:
            if c in f.ingredients:
                for a in f.allergens:
                    if a in a_count:
                        a_count[a] += 1
                    else:
                        a_count[a] = 1
        for a in a_count:
            if a_count[a] == allergen_counts[a] and c in candidates_part1:
                del candidates_part1[c]
    
    part1 = 0
    for c in candidates_part1:
        for f in foods:
            if c in f.ingredients:
                part1 +=1 
    print("Part 1: %d" % part1)
    
    # part 2 - iteratively determine unassigned ingredients that uniquely appear in all instances of an allergen
    assignments = {}
    
    # remove all part1 ingredients from contention
    for c in candidates_part1:
        if c in candidates:
            del candidates[c]
            
    while(len(assignments) < len(allergen_counts)):
        for a in allergen_counts:
            unassigned_ingredient_count = {}
            for f in foods:
                if a in f.allergens:
                    for i in f.ingredients:
                        if i in assignments or i in candidates_part1:
                            continue
                        if i in unassigned_ingredient_count:
                            unassigned_ingredient_count[i] += 1
                        elif i not in assignments and i not in candidates_part1:
                            unassigned_ingredient_count[i] = 1
            possibles = []
            for i in unassigned_ingredient_count:
                if unassigned_ingredient_count[i] >= allergen_counts[a]:
                    possibles.append(i)
            if len(possibles) == 1:
                assignments[possibles[0]] = a
    
    #build string
    part2_str = ''
    allergen_list = allergen_counts.keys()
    allergen_list2 = []
    for a in allergen_list:
        allergen_list2.append(a)
    allergen_list2.sort()
    for a in allergen_list2:
        for i in assignments:
            if assignments[i] == a:
                part2_str += i+',' 
    if(len(part2_str) > 1):
        part2_str = part2_str[:-1] # remove final comma
        
    print("Part 2: %s" % part2_str)
