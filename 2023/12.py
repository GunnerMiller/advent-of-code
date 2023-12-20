input = open("12.txt", "r").readlines()
# input = open("12.sample.txt", "r").readlines()
p1 = 0
p2 = 0

# read line, split with spacec
for line in input:
    line, rule = line.split()
    line = [*line]

    perms = [line]
    for i, char in enumerate(line):
        if char == '?':
            temp = []
            while len(perms) > 0:
                curr = perms.pop()
                p = curr.copy()
                p[i] = '.'
                q = curr.copy()
                q[i] = '#'
                temp.append(p)
                temp.append(q)
            perms = temp.copy()

    for perm in perms:
        hashes = ' '.join(''.join(perm).split('.')).split()
        groups = rule.split(",")
        clear = True
        if len(hashes) == len(groups):
            for i in range(len(hashes)):
                if (len(hashes[i]) != int(groups[i])):
                    clear = False
                    break
        else:
            clear = False

        if clear:
            p1 += 1
    
print(p1)