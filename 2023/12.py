# input = open("12.txt", "r").readlines()
input = open("12.sample.txt", "r").readlines()
p1 = 0
p2 = 0

# read line, split with spacec
for line in input:
    line, rule = line.split()
    line = [*line]
    
    perms = [line]
    while len(perms) > 0:
        curr = perms.pop()
        p = line.copy()
        p[i] = '.'
        q = line.copy()
        q[i] = '#'
        perms.append(p)
        perms.append(q)

    for perm in perms:
        print(perm)
# resolve wild cards, finding all permutations of the input line
    

    # find how many lines satify the rules given in split[1] from L6
    
    # use this to get the groups of hashes
    # hashes = ' '.join(line.split(".")).split()

    # groups = [rule.split(",")]
    # for group in groups
    # pop groups
    # try to find match through hashes
    # end loop
    # if groups not empty all rules
    # p1 + sum of lines that satisfy