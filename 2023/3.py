import numpy
import unittest

out1 = 0
out2 = 0
inputs = open("3.txt", "r").readlines()

parts = []
results = {}
symbols = numpy.array(["*", "$", "+", "#", "=", "-", "%", "&", "@", "/"])
for lineIndex, line in enumerate(inputs):
    i = 0
    while i < len(line):
        if(line[i].isdigit()):
            buffer = line[i]
            start = i
            while i+1 < len(line) and line[i+1].isdigit():
                buffer += line[i+1]
                i += 1
            end = i
            ele = buffer

            is_part = False
            for x in range(0,3):
                try:    
                    currLine = numpy.array([*inputs[lineIndex-1+x]])
                    result =  numpy.nonzero(numpy.in1d(currLine, symbols))[0]
                    for res in result:
                        if int(res) in range(start - 1, end + 2):
                            is_part = True
                except:
                    continue
            if is_part:
                parts.append(ele)
        i += 1
for part in parts:
    out1 += int(part)

class tests(unittest.TestCase):
    def testPartOne(self):
        self.assertEqual(out1, 556057)
    # def testPartTwo(self):
    #     self.assertEqual(out2, 70924)
if __name__ == '__main__':
    unittest.main()