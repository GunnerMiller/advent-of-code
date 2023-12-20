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
for empty_row in reversed(empty_rows):
    rows.insert(empty_row, [*'.' * len(rows[0])])
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
for ec in reversed(empty_cols):
    for row in rows:
        row.insert(ec, '.')

# find coordinates of all hashes
galaxies = []
for y, row in enumerate(rows):
    for x, col in enumerate(row):  
        if rows[y][x] == '#':
            galaxies.append([x,y])

while len(galaxies) > 0:
    curr = galaxies.pop()
    temp = []
    while len(galaxies) > 0:
        next = galaxies.pop()
        temp.append(next)
        p1 += abs(next[0] - curr[0]) + abs(next[1] - curr[1])
    for e in temp:
        galaxies.append(e)

print(p1)