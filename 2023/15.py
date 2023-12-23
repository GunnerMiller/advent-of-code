from collections import defaultdict
# filename = '15.txt'
filename = '15.sample.txt'
try:
    input = open(filename, "r").read().replace("\n",'')
except:
    input = open('2023/'+filename, "r").read().replace("\n",'')
p1 = 0
for line in input.split(','):
    curr = 0
    for char in line:
        curr = (curr + ord(char)) * 17 % 256
    p1 += curr
# print(p1)

p2 = 0
map = defaultdict(list)
for step, line in enumerate(input.split(',')):
    key = line[0:2]
    command = line[2:]
    bucket = 0
    for char in key:
        bucket = (bucket + ord(char)) * 17 % 256
    if command[0] == '=':
        focus = command[-1]
        if key not in (i[0] for i in map[bucket]):
            map[bucket].append([key, focus])
        else:
            i = map[bucket].index(key)
            map[bucket][i][1] = focus
    else:
        try:
            map[bucket].remove(key)
        except:
            pass
    
for i, bucket in enumerate(map.keys()):
    if len(map[bucket]) == 0:
        continue
    for i, ele in enumerate(map[bucket]):
        box = bucket + 1
        slot = i + 1
        focus = ele[1]
        value = box * slot * focus
        print(value)
print(p2)