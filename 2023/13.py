input = open("13.txt", "r").readlines()
# input = open("13.sample.txt", "r").readlines()
p1 = 0
p2 = 0

grids = [[]]
gi = 0
for line in input:
    line = line.strip()
    if len(line) > 0:
        grids[gi].append(line)
    else:
        gi += 1
        grids.append([])

for grid_index, grid in enumerate(grids):
    if (grid_index + 1) % 2 != 0:
        cols = {}
        c_mirrors = []
        for c in range(len(grid[0])): 
            l = []
            for r in range(len(grid)):
                l.append(grid[r][c])
            l = ''.join(l)
            print(l)
            try:
                j = cols[l]
                if j == c-1:
                    c_mirrors.append([j,c])
                    p1+=c
            except:
                cols[l] = c
        print(c_mirrors)
    else:
        rows = {}   
        r_mirrors = []
        for i, line in enumerate(grid):
            print(line)
            try:
                j = rows[line]
                if j == i-1:
                    r_mirrors.append([j,i])
                    p1+=i*100
            except:
                rows[line] = i
        print(r_mirrors)
print(p1)