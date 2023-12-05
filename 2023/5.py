from collections import defaultdict

out1 = 0
out2 = 0
inputs = open("5.txt", "r").readlines()
# inputs = open("5.sample.txt", "r").readlines()

seeds = []
maps = {}
mappings = defaultdict(str, {"seed":"soil","soil":"fertilizer","fertilizer":"water","water":"light","light":"temperature","temperature":"humidity", "humidity":"location"})

i = 0
while i < len(inputs):
    line = inputs[i]
    if i == 0:
        seeds = line.split(":")[1].strip().split()
    elif line != "\n": 
        if not line[0].isdigit():
            key = line.split()[0].split("-")[2]
            map = defaultdict(str)
            while i+1 < len(inputs) and inputs[i+1][0].isdigit():
                dest, source, range_length = inputs[i+1].split()
                map[source] = [dest, range_length]
                i+=1

            maps[key] = map
    i += 1

curr_low = None
for seedValue in seeds:
    value = seedValue
    key = "seed"
    next_map = mappings[key]

    # drill to location
    while next_map != "":
        map = maps[next_map]
        for source in map.keys():
            dest, range_length = map[source]
            source = int(source)
            value = int(value)
            if value >= source and value <= source + int(range_length) - 1:
                value = value + int(dest) - int(source)
                break
        
        next_map = mappings[next_map]

    if curr_low == None:
        curr_low = value
    else:
        curr_low = min(curr_low, value)

print(curr_low)
print(out2)