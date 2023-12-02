out1 = 0
out2 = 0
inputs = open("2.txt", "r").read().split('\n')

redCount = 12
greenCount = 13
blueCount = 14
for gameIndex, game in enumerate(inputs):
    game = game[game.index(":")+2:]
    gamePossible = True
    maxRedCount = 0
    maxGreenCount = 0
    maxBlueCount = 0

    sets = game.split(";")
    for set in sets:
        redsInSet = 0
        greensInSet = 0
        bluesInSet = 0

        cubes = set.split(",")
        for cube in cubes:
            x, color = cube.strip().split(" ")
            if color == "red":
                redsInSet += int(x)
                if maxRedCount == 0:
                    maxRedCount = int(x)
                elif int(x) > maxRedCount:
                    maxRedCount = int(x)
            elif color == "green":
                greensInSet += int(x)
                if maxGreenCount == 0:
                    maxGreenCount = int(x)
                elif int(x) > maxGreenCount:
                    maxGreenCount = int(x)
            elif color == "blue":
                bluesInSet += int(x)
                if maxBlueCount == 0:
                    maxBlueCount = int(x)
                elif int(x) > maxBlueCount:
                    maxBlueCount = int(x)
        if redsInSet > redCount:
            gamePossible = False
        if greensInSet > greenCount:
            gamePossible = False
        if bluesInSet > blueCount:
            gamePossible = False
    if gamePossible == True:
        out1 += gameIndex + 1
    out2 += (maxRedCount * maxGreenCount * maxBlueCount)

print(out1)
print(out2)