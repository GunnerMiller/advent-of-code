import math
p1 = 0

input = open("7.txt", "r").readlines()
# input = open("7.sample.txt", "r").readlines()

times = input[0].split(":")[1].strip().split()
dists = input[1].split(":")[1].strip().split()
Beats = []
for i in range(len(times)):
    time = int(times[i])
    dist = int(dists[i])
    beats = 0
    traveled = 0
    for j in range(1,int(time)):
        acc = j
        traveled = acc * (time - j)
        if traveled > dist:
            beats += 1
    Beats.append(beats)

p1 += math.prod(Beats)
print(p1)