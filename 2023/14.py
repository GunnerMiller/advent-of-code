input = open("14.txt", "r").readlines()
# input = open("../14.sample.txt", "r").readlines()
out = 0

def find_slot(line, index):
    copy = line
    copy = copy[:index]
    # print(copy)
    for x, char in enumerate(reversed(copy)):
        if char == '#' or char == 'O':
            return index - x
    return index - len(copy)

def swap(line, a, b):
    if a != b:
        temp = line[a]
        line[a] = line[b]
        line[b] = temp

         
rotato = zip(*input)
grid = []
for line in rotato:
    line = list(line)

    for i, char in enumerate(line):
        if char == 'O':
            swap(line, find_slot(line,i), i)
    for i, char in enumerate(line):
        if char == 'O':
            out += (len(line) - i)
print(out)