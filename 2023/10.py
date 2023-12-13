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

#################
# use validation to confirm it's legit, get to go 
#################
if(pipes.find(get_up(start_x,start_y))) > -1:
    starters.append([start_x, start_y-1])
if(pipes.find(get_left(start_x,start_y))) > -1:
    starters.append([start_x-1, start_y])
if(pipes.find(get_right(start_x,start_y))) > -1:
    starters.append([start_x+1, start_y])
if(pipes.find(get_down(start_x,start_y))) > -1:
    starters.append([start_x, start_y+1])

# MAPS:
# pieces{} {"L":{"up":"right"}{"right","up"}}
# directions{}"down":"go_down"

# sdir = source direction
# ndir = next direction
curr = starters.pop()
sdir_x = curr[0] - start_x
sdir_y = curr[1] - start_y
ndir = None
if sdir_x == 1:
    ndir = "right"
elif sdir_x == -1:
    ndir = "left"
elif sdir_y == 1:
    ndir = "down"
elif sdir_x == -1:
    ndir = "up"
# directions[ndir]()
# if it returns a direction, start loop
# track steps along the way
# if it terminates without returning we go to the next starter

# TRAVERSE:
    # functions:
    # IN: x and y from curr_p
    # def go_down(x, y)
    # sdir = "up"
    # ndir = pieces[get_down(x,y)][sdir]
    # keyError or indexError here validates that the piece isn't connected
    # catch those errors and return None
    # ndirfun =  directions[ndir]
    # return ndirfun 
    # we return for < stack space