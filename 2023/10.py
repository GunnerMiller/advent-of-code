import math
grid = []
def get_at_coord(x,y):
    return grid[y][x]

input = open("10.txt", "r").readlines()
# input = open("10.sample.txt", "r").readlines()

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
if(pipes.find(get_at_coord(x,y-1))) > -1:
    starters.append([start_x, start_y-1])
if(pipes.find(get_at_coord(x-1,y))) > -1:
    starters.append([start_x-1, start_y])
if(pipes.find(get_at_coord(x+1,y))) > -1:
    starters.append([start_x+1, start_y])
if(pipes.find(get_at_coord(x,y+1))) > -1:
    starters.append([start_x, start_y+1])

u = "up"
d = "down"
l = "left"
r = "right"
pieces = {"|":{u:d,d:u},"-":{l:r,r:l},"L":{u:r,r:u},"J":{u:l,l:u},"F":{d:r,r:d},"7":{d:l,l:d}}

def go_up(x,y):
    sdir = d
    try:
        return pieces[get_at_coord(x,y)][sdir]
    except:
        return None
def go_left(x,y):
    sdir = r
    try:
        return pieces[get_at_coord(x,y)][sdir]
    except:
        return None
def go_right(x,y):
    sdir = l
    try:
        return pieces[get_at_coord(x,y)][sdir]
    except:
        return None
def go_down(x,y):
    sdir = u
    try:
        return pieces[get_at_coord(x,y)][sdir]
    except:
        return None
go = {u:go_up, d:go_down, l:go_left, r:go_right}

curr = starters.pop()
sdir_x = curr[0] - start_x
sdir_y = curr[1] - start_y
ndir = None
print(get_at_coord(curr[0], curr[1]))
if sdir_x == 1:
    ndir = r
elif sdir_x == -1:
    ndir = l
elif sdir_y == 1:
    ndir = d
elif sdir_x == -1:
    ndir = u

x = curr[0]
y = curr[1]
steps = 0
while (ndir is not None):
    steps += 1
    if ndir == u:
        y -= 1
    elif ndir == d:
        y += 1
    elif ndir == l:
        x -= 1
    elif ndir == r:
        x += 1
    ndir = (go[ndir](x,y))

if get_at_coord(x,y) == 'S':
    print(math.ceil(steps/2))