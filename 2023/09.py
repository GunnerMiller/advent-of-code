import sys
input = open("9.txt", "r").readlines()
# input = open("9.sample.txt", "r").readlines()

def is_zeroed(arr):
    if arr == []:
        return False
    
    zeroed = True
    for ele in arr:
        if ele != 0:
            zeroed = False
            break

    return zeroed

    


p1 = 0
p2 = 0
for line in input:
    line = line.strip().split()
    lines = [[int(i) for i in line]]

    p1 += int(line[-1])
    while(not is_zeroed(line)):
        curr = None
        new_line = []
        for ele in line:
            if curr == None:
                curr = ele
            else:
                new_line.append(int(ele) - int(curr))
                curr = ele
        line = new_line
        p1 += new_line[-1]
        lines.append(new_line)
    
    start_extrapolation = 0
    curr_line = None
    for line in reversed(lines):
        print(line)
        if curr_line == None:
            curr_line = line
        else:
            start_extrapolation = (line[0] - start_extrapolation)
            print(start_extrapolation)
    p2 += start_extrapolation
print(p1)
print(p2)