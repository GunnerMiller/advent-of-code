from collections import defaultdict
input = open("15.sample.txt", "r").read().replace("\n",'')
p1 = 0
for line in input.split(','):
    curr = 0
    for char in line:
        curr = (curr + ord(char)) * 17 % 256
    p1 += curr
# print(p1)

p2 = 0
map = defaultdict(str)
for line in input.split(','):
    key = line[0:2]
    command = line[2:]
    box = 0
    for char in key:
        box = (box + ord(char)) * 17 % 256
    if command[0] == '=':
        lens = command[-1]
        map[key] = [box, lens]
    else:
        try:
            del map[key]
        except:
            pass
for key in map.keys():
    print(key + ' ' + str(map[key][0]) + ' ' + str(map[key][1]))