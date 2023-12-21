# input = open("13.txt", "r").readlines()
input = open("13.sample.txt", "r").readlines()
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
        for c in range(len(grid[0])): 
            l = []
            for r in range(len(grid)):
                l.append(grid[r][c])
            l = ''.join(l)
            print(l)
            try:
                j = cols[l]
                if j == c-1:
                    p1 += (c+1)*100
                    print(p1)
                    break
            except:
                cols[l] = c
    else:
        rows = {}   
        for i, line in enumerate(grid):
            print(line)
            try:
                j = rows[line]
                if j == i-1:
                    p1 += i + 1 
                    print(p1)
                    break
            except:
                rows[line] = i