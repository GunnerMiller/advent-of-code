file = open("2.txt", "r")
content = file.read()
inputs = content.split('\n')
out1 = 0
out2 = 0
redCount = 12
greenCount = 13
blueCount = 14
for gameIndex, game in enumerate(inputs):
    #gameIndex + 1
    game = game[game.index(":")+2:]
    badgame = 0
    sets = game.split(";")
    for set in sets:
        # print(set)
        currentRedCount = 0
        currentGreenCount = 0
        currentBlueCount = 0
        pulls = set.split(",")
        for pull in pulls:
            x = pull.strip().split(" ")
            if x[1] == "red":
                currentRedCount += int(x[0])
            if x[1] == "green":
                currentGreenCount += int(x[0])
            if x[1] == "blue":
                currentBlueCount += int(x[0])
        if currentRedCount > redCount:
            badgame = 1
        if currentGreenCount > greenCount:
            badgame = 1
        if currentBlueCount > blueCount:
            badgame = 1
    if badgame == 0:
        out1 += gameIndex + 1
        

    

        
print(out1)
print(out2)