import sys
from collections import defaultdict


values = {"A":14,"K":13,"Q":12,"T":11, "9":10, "8":9, "7":8, "6":7, "5":6,"4":5, "3":4, "2":3, "1":2, "J":1}
five_kind = {}
four_kind = {}
full_house = {}
three_kind = {}
two_pair = {}
pair = {}
high_card_ass_losers  = {}
p1 = 0
input = open("7.txt", "r").readlines()
# input = open("7.sample.txt", "r").readlines()

def pack(arr, depth):
    map = defaultdict(list)
    for ele in arr:
        map[ele[depth]].append(ele)
    for key in map.keys():
        if len(map[key]) > 1:
            map[key] = pack(map[key], depth+1)
    return map

rankings = []
def unpack(map):
    keys = list(map.keys())
    keys.sort(key=lambda val:values[val[0]]) 
    for key in keys:
        if len(map[key]) == 1 and type(map[key]) != defaultdict:
            rankings.append(map[key[0]])
        else:
            unpack(map[key])

hands = {}
for line in input:
    hand, bid = line.split()
    counts = defaultdict(str)
    jokers = 0
    for card in hand:
        if card == 'J':
            jokers += 1
        if counts[card] == '':
            counts[card] = 1
        else:
            counts[card] = int(counts[card]) + 1

    if jokers > 0 and jokers != 5:
        del counts['J']
        key = max(counts, key=counts.get)
        counts[key] = counts[key] + int(jokers)
    matches = 0
    for val in counts.values():
        print(val)
        if val > 1:
            matches += 1
    if matches == 1:
        if len(counts.values()) == 1:
            five_kind[hand] = bid
        else:
            if max(list(counts.values())) == 4:
                four_kind[hand] = bid
            elif max(list(counts.values())) == 3:
                three_kind[hand] = bid
            else:
                pair[hand] = bid
    elif matches == 2:
        if len(counts.values()) == 2:
            full_house[hand] = bid
        else:
            two_pair[hand] = bid
    else:
        high_card_ass_losers[hand] = bid
    hands[hand] = bid

five_kind = pack(list(five_kind.keys()), 0)
four_kind = pack(list(four_kind.keys()), 0)
full_house = pack(list(full_house.keys()), 0)
three_kind = pack(list(three_kind.keys()), 0)
two_pair = pack(list(two_pair.keys()), 0)
pair = pack(list(pair.keys()), 0)
high_card_ass_losers = pack(list(high_card_ass_losers.keys()), 0)
unpack(high_card_ass_losers)
unpack(pair)
unpack(two_pair)
unpack(three_kind)
unpack(full_house)
unpack(four_kind)
unpack(five_kind)

for i, rank in enumerate(rankings):
    p1 += int(hands[rank[0]]) * (i + 1)
print(p1)