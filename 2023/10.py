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

u = "up"
d = "down"
l = "left"
r = "right"
pieces = {"|":{u:d,d:u},"-":{l:r,r:l},"L":{u:r,r:u},"J":{u:l,l:u},"F":{d:r,r:d},"7":{d:l,l:d}}

directions = {}
def go_up(x,y):
    sdir = d
    try:
        ndir = pieces[get_up(x,y)][sdir]
    except:
        return None
    ndirfun = directions[ndir]
    return ndirfun
def go_left(x,y):
    sdir = r
    try:
        ndir = pieces[get_left(x,y)][sdir]
    except:
        return None
    ndirfun = directions[ndir]
    return ndirfun
def go_right(x,y):
    sdir = l
    try:
        ndir = pieces[get_right(x,y)][sdir]
    except:
        return None
    ndirfun = directions[ndir]
    return ndirfun
def go_down(x,y):
    sdir = u
    try:
        ndir = pieces[get_down(x,y)][sdir]
    except:
        return None
    ndirfun = directions[ndir]
    return ndirfun
directions = {u:go_up, d:go_down, l:go_left, r:go_right}

# directions[ndir]()
# if it returns a direction, start loop
# track steps along the way
# if it terminates without returning we go to the next starter
curr = starters.pop()
sdir_x = curr[0] - start_x
sdir_y = curr[1] - start_y
ndir = None
print(get_coord(curr[0], curr[1]))
if sdir_x == 1:
    ndir = r
elif sdir_x == -1:
    ndir = l
elif sdir_y == 1:
    ndir = d
elif sdir_x == -1:
    ndir = u
if ndir is not None:
    print(directions[ndir](sdir_x,sdir_y))