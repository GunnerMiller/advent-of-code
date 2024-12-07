from collections import defaultdict

file = "01.txt"
lines = open(file, "r")

arr1 = []
arr2 = []
for line in lines:
    split = line.split("   ")
    arr1.append(split[0])
    arr2.append(split[-1].strip())

sorted1 = arr1.copy()
sorted1.sort()
sorted2 = arr2.copy()
sorted2.sort()

tally = 0
for i in range(len(sorted1)):
    tally = tally + abs(int(sorted1[i]) - int(sorted2[i]))

print("part 1 answer:")
print(tally)

counts = defaultdict(int)
for num in arr2:
    counts[num] = counts[num] + 1

tally2 = 0
for num in arr1:
    tally2 = tally2 + (int(num) * counts[num])
print("part 2 answer:")
print(tally2)