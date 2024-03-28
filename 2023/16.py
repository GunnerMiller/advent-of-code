# filename = '16.txt'
filename = '16.sample.txt'
try:
    input = open(filename, "r").readlines()
except:
    input = open('2023/'+filename, "r").readlines()
p1 = 0

r = "right"
l = "left"
u = "up"
d = "down"
lasers = [([0,0],r)]
def split_vert(x,y):
    pass
def split_horz(x,y):
    pass
def get_cord(x,y):
    return input[y][x]
def go_down(x,y):
    return get_cord(x,y-1)
def go_up(x,y):
    return get_cord(x,y+1)
def go_left(x,y):
    return get_cord(x-1,y)
def go_right(x,y):
    return get_cord(x+1,y)
dir_fun = {d:go_down,u:go_up,r:go_right,l:go_left}
pieces = {
    "|":{l:split_vert,r:split_vert,d:go_down,u:go_up},
    "-":{u:split_horz,d:split_horz,r:go_right,l:go_left},
    "/":{u:go_left,l:go_up,d:go_right,r:go_down},
    "\\":{u:go_right,r:go_up,l:go_down,d:go_left}
}

for line in input:
    print(line.strip())

pieces = {""}
energized = {}
while len(lasers) > 0:
    laser = lasers.pop()
    alive = True
    dir = laser[1]
    curr_x = laser[0][0]
    curr_y = laser[0][1]
    while (alive):
        next = dir_fun[dir](curr_x,curr_y)
        print(next)
        try:
            continue
        except:
            alive = False 