# input = open("15.sample.txt", "r").read().replace("\n",'')
input = open("15.txt", "r").read().replace("\n",'')
p1 = 0
for line in input.split(','):
    curr = 0
    for char in line:
        curr += ord(char) 
        curr *= 17
        curr = curr % 256
    p1 += curr
print(p1)