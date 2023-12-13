from collections import defaultdict
import datetime
import math

start = datetime.datetime.now()
d =  {}
cards = {}

# inputs = open("4.sample.txt", "r").readlines()
inputs = open("4.txt", "r").readlines()

out1 = 0
out2 = 0
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

stack = []
for i in range(1, len(inputs)+1):
    stack.append(i)



while len(stack) > 0:
    out2 += 1
    curr_card = stack.pop()
    num_matches = cards[curr_card]
    if num_matches > 0:
        # print ("curr_card=" + str(curr_card) + " num_matches=" + str(num_matches))
        for i in range(1, 1 + num_matches):
            stack.append(curr_card + i)
        
    

end = datetime.datetime.now()
result = end-start

print(int(out1))
print(int(out2))
print("TIME (sec)= " + str(result.total_seconds()))
print("TIME (ms)= " + str(int(result.total_seconds())* 1000))