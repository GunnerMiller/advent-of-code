grid = []
def get_coord(x,y):
    return grid[y][x]
def get_up(x,y):
    return get_coord(start_x,start_y-1)
def get_left(x,y):
    return get_coord(start_x-1,start_y)
def get_right(x,y):
    return get_coord(start_x+1,start_y)
def get_down(x,y):
    return get_coord(start_x,start_y+1)

# input = open("10.txt", "r").readlines()
input = open("10.sample.txt", "r").readlines()
p1 = 0
p2 = 0

for line in input:
    grid.append([*line.strip()])

start_x = 0
start_y = 0
for y, line in enumerate(grid):
    for x, pt in enumerate(line):
        if pt == 'S':
            start_x = x
            start_y = y

pipes = "|-LJF7"
starters = []
if(pipes.find(get_up(start_x,start_y))) > -1:
    starters.append([start_x, start_y-1])
if(pipes.find(get_left(start_x,start_y))) > -1:
    starters.append([start_x-1, start_y])
if(pipes.find(get_right(start_x,start_y))) > -1:
    starters.append([start_x+1, start_y])
if(pipes.find(get_down(start_x,start_y))) > -1:
    starters.append([start_x, start_y+1])

valid_vertical = "|LJF7"
valid_horizontal = "-LJF7"

connectors = []
source_x = start_x
source_y = start_y
for start in starters:
    # we need methods to track our source and make the appropriate step
    continue