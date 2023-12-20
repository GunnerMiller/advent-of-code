# input = open("12.txt", "r").readlines()
input = open("12.sample.txt", "r").readlines()
p1 = 0
p2 = 0

# read line, split with spacec
for line in input:
    line, rule = line.split()
    print(line)
    print(rule)
# resolve wild cards, finding all permutations of the input line
# find how many lines satify the rules given in split[1] from L6
# p1 + sum of lines that satisfy