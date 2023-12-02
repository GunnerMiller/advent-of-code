import unittest
import math
from collections import defaultdict

out1 = 0
out2 = 0
inputs = open("2.txt", "r").read().split('\n')

for gameIndex, game in enumerate(inputs):
    game = game[(game.index(":")+2):]
    gameIsPossible = True
    colorsNeeded = defaultdict(int)

    for set in game.split(";"):
        for cube in set.split(","):
            num, color = cube.split()
            colorsNeeded[color] = max(colorsNeeded[color], int(num))
            if int(num) > {'red': 12, 'green': 13, 'blue': 14}.get(color):
                gameIsPossible = False
        
    if gameIsPossible:
        out1 += gameIndex + 1
    out2 += math.prod(colorsNeeded.values())

class tests(unittest.TestCase):
    def testPartOne(self):
        self.assertEqual(out1, 2771)
    def testPartTwo(self):
        self.assertEqual(out2, 70924)
if __name__ == '__main__':
    unittest.main()