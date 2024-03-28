input = open("11.txt", "r").readlines()
# input = open("11.sample.txt", "r").readlines()
p1 = 0
p2 = 0

rows = []
for line in input:
    rows.append([*line.strip()])
empty_rows = []
for i, row in enumerate(rows):
    empty = True
    for char in row:
        if char != '.':
            empty = False
            break
    if empty:
        empty_rows.append(i)
empty_cols = []
for col in range(len(rows[0])):
    empty = True
    for row in range(len(rows)):
        char = rows[row][col]
        if char != '.':
            empty = False
            break
    if empty:
        empty_cols.append(col)

# find coordinates of all hashes
galaxies = []
for y, row in enumerate(rows):
    for x, col in enumerate(row):  
        if rows[y][x] == '#':
            galaxies.append([x,y])

expansion_factor = 1000000 - 1
while len(galaxies) > 0:
    curr = galaxies.pop()
    temp = []
    while len(galaxies) > 0:
        next = galaxies.pop()
        temp.append(next)
        x1 = curr[0]
        x2 = next[0]
        y1 = curr[1]
        y2 = next[1]
        for r in empty_rows:
            if r in range(min(y1,y2), max(y1,y2)):
                p1 += expansion_factor
        for c in empty_cols:
            if c in range(min(x1,x2), max(x1,x2)):
                p1 += expansion_factor
        p1 += abs(x1-x2) + abs(y1-y2)
    for e in temp:
        galaxies.append(e)

print(p1)