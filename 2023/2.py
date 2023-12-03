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
    maxRedCount = 0
    maxGreenCount = 0
    maxBlueCount = 0
    for set in sets:
        currentRedCount = 0
        currentGreenCount = 0
        currentBlueCount = 0
        pulls = set.split(",")
        for pull in pulls:
            x = pull.strip().split(" ")
            if x[1] == "red":
                currentRedCount += int(x[0])
                if maxRedCount == 0:
                    maxRedCount = int(x[0])
                elif int(x[0]) > maxRedCount:
                    maxRedCount = int(x[0])
            elif x[1] == "green":
                currentGreenCount += int(x[0])
                if maxGreenCount == 0:
                    maxGreenCount = int(x[0])
                elif int(x[0]) > maxGreenCount:
                    maxGreenCount = int(x[0])
            elif x[1] == "blue":
                currentBlueCount += int(x[0])
                if maxBlueCount == 0:
                    maxBlueCount = int(x[0])
                elif int(x[0]) > maxBlueCount:
                    maxBlueCount = int(x[0])
        if currentRedCount > redCount:
            badgame = 1
        if currentGreenCount > greenCount:
            badgame = 1
        if currentBlueCount > blueCount:
            badgame = 1
    if badgame == 0:
        out1 += gameIndex + 1
    power = maxRedCount * maxGreenCount * maxBlueCount
    out2 += (power)
        

    

        
print(out1)
print(out2)