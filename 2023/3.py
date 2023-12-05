import sys
import numpy
from termcolor import colored


def printSameLine(input):
    print(input, end="")

out1 = 0
out2 = 0
inputs = open("3.txt", "r").readlines()
symbols = numpy.array(["*", "$", "+", "#", "=", "-", "%", "&", "@", "/"])
parts = []

for lineIndex, line in enumerate(inputs):
    printIndex = 0
    # printSameLine("Line #" + str(lineIndex+1) + ": ")
    # print("LINE #" + str(lineIndex+1) + ": " + line[:-1])
    i = 0
    while i < len(line):
        start = i
        buffer = ""
        ele = line[i]
        # printSameLine(ele)
        # print(ele)
        if(ele.isdigit()):
            buffer += ele
            while i+1 < len(line) and line[i+1].isdigit():
                buffer += line[i+1]
                i += 1
            ele = buffer
            # printSameLine(ele + " ")
            end = i

            print(ele + " START: " + str(start) + " END: " + str(end))

            # line before
            clear_pre = True
            if lineIndex -1 > 0: 
                currLine = numpy.array([*inputs[lineIndex-1]])
                result =  numpy.nonzero(numpy.in1d(currLine, symbols))[0]
                # print(result)
                if len(result) > 0:
                    for res in result:
                        if int(res) in range(start - 1, end + 2):
                            clear_pre = False

            clear_current = True
            currLine = numpy.array([*inputs[lineIndex]])
            result =  numpy.nonzero(numpy.in1d(currLine, symbols))[0]
            # print(result)
            if len(result) > 0:
                for res in result:
                    if int(res) in range(start - 1, end + 2):
                        clear_current = False

            # line after
            clear_post = True
            if lineIndex + 1 < len(inputs):
                currLine = numpy.array([*inputs[lineIndex+1]])
                result =  numpy.nonzero(numpy.in1d(currLine, symbols))[0]
                # print(result)
                if len(result) > 0:
                    for res in result:
                        if int(res) in range(start - 1, end + 2):
                            clear_post = False  

            if not clear_pre or not clear_post or not clear_current:
                parts.append(ele)

            i += 1
        else:
            i += 1
    printSameLine("\n")
    # if lineIndex > 3:
    #     sys.exit()
                    
                    

for part in parts:
    out1 += int(part)

print(out1)
print(out2)

# zero =  "....."
# single = ".1..."
# double = ".12.."
# triple = ".123."
# symbol_first   = "*...."
# symbol_second  = ".*..."
# symbol_third   = "..*.."
# symbol_fourth  = "...*."
# symbol_fifth   = "....*"
# class tests(unittest.TestCase):

#     def testSymbolFirstIndex(self):
#         currLine = numpy.array([*symbol_first])
#         result =  numpy.nonzero(numpy.in1d(currLine, symbols))[0]
#         result_first  = int(result[0] in range())
#         result_second = 
#         result_third  = 
#         result_fourth = 
#         result_fifth  = 
# if __name__ == '__main__':
#     unittest.main()