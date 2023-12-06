from collections import defaultdict
import math

d =  {}
cards = {}

# inputs = open("4.sample.txt", "r").readlines()
inputs = open("4.txt", "r").readlines()

out1 = 0
for i, card in enumerate(inputs, 1):
    card = card.split(':')[1].strip()	
    winners, nums = card.split("|")

    matches = 0
    for winner in winners.split():
        try:
            d[i][winner] = winner
        except:
            d[i] = defaultdict(str)
            d[i][winner] = winner

    for num in nums.split():
        if d[i][num] != '':
            matches += 1
    if matches == 1:
        out1 += 1
    elif matches > 1:
        out1 += (1 * math.pow(2, matches - 1))
    cards[i] = matches

print(int(out1))