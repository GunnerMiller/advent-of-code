from collections import defaultdict
filename = '15.txt'
# filename = '15.sample.txt'
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
print(p1)

p2 = 0
map = defaultdict(list)
for step, line in enumerate(input.split(',')):
    add = True
    if line[-1] == '-':
        key = line[:-1]
        add = False
    else:
        key, focus = line.split('=')
    bucket = 0
    for char in key:
        bucket = (bucket + ord(char)) * 17 % 256
    in_bucket = [i[0] for i in map[bucket]]
    if add:
        if key not in (in_bucket):
            map[bucket].append([key, focus])
        else:
            i = in_bucket.index(key)
            map[bucket][i][1] = focus
    else:
        try:
            i = in_bucket.index(key)
            del map[bucket][i]
        except Exception as e:
            pass
    
for i, bucket in enumerate(map.keys()):
    if len(map[bucket]) == 0:
        continue
    for i, ele in enumerate(map[bucket]):
        box = int(bucket) + 1
        slot = i + 1
        focus = int(ele[1])
        value = box * slot * focus
        print(value)
        p2 += value
print(p2)