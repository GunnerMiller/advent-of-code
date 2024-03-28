# input = open("8.txt", "r").readlines()
input = open("8.sample.txt", "r").readlines()

step = input[0].strip()
forks = {}
starts = []
ends = []
for i in range(1, len(input)):
    line = input[i]
    start, options = line.split("=")
    start = start.strip()
    options = options.split(",")
    left = options[0].strip()[1:]
    right = options[1].strip()[0:3]
    forks[start.strip()] = [left, right]
    for char in start:
        if char == "A":
            starts.append(start)
            break
        if char == "Z":
            ends.append(start)
            break


steps_taken = 0
shortcut = {}
curr = starts[0]
while curr not in ends:
    # Check shortcuts

    # Perform step
    # set start
    for char in step:
        if(char == "L"):
            curr = forks[curr][0]
        elif(char == "R"):
            curr = forks[curr][1]
    steps_taken += 1
    # set end
    # add to shortcuts where key is start and value is end

print(steps_taken * len(step))