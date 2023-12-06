import sys
import math
p1 = 0

input = open("6.txt", "r").readlines()
# input = open("6.sample.txt", "r").readlines()

times = input[0].split(":")[1].replace(" ", "").strip()
dists = input[1].split(":")[1].replace(" ", "").strip()
print(times)
print(dists)

time = int(times)
dist = int(dists)
beats = 0
traveled = 0
for j in range(1,int(time)):
    acc = j
    traveled = acc * (time - j)
    if traveled > dist:
        beats += 1

p1 += beats
print(p1)