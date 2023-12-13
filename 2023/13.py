import numpy as np
# input = open("13.txt", "r").readlines()
input = open("13.sample.txt", "r").readlines()
p1 = 0
p2 = 0

matched = False
cols = []
rows = []

grid = []
curr = input[0]
for line in input
    grid.append(line)
# maybe optimize to check rows first?

# Go by columns and seek match
# numpy is good for finding hashes
# get sum of indeces where hashes are
# save sum to array of length columns
# each index of array is sum at that index
# use array for lookup of previously summed columns
# repeat for rows if columns don't match/mirror