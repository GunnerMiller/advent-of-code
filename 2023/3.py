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
    printSameLine("Line #" + str(lineIndex+1) + ": ")
    # print("LINE #" + str(lineIndex+1) + ": " + line[:-1])
    for eleIndex, ele in enumerate(line.split(".")):
        if ele != "" and ele != "\n":
            if(ele.isdigit()):
                start = line.find("." + ele + ".") + 1
                end = start + len(ele) - 1

                printSameLine(line[printIndex:start])
                printIndex = start + len(ele)

                clear_pre = True
                clear_post = True
                
                # line before
                if lineIndex -1 > 0: 
                    currLine = numpy.array([*inputs[lineIndex-1]])
                    result =  numpy.nonzero(numpy.in1d(currLine, symbols))[0]
                    # print(result)
                    if len(result) > 0:
                        for res in result:
                            if int(res) in range(start-1,end+2):
                                clear_pre = False

                # line after
                if lineIndex + 1 < len(inputs):
                    currLine = numpy.array([*inputs[lineIndex+1]])
                    result =  numpy.nonzero(numpy.in1d(currLine, symbols))[0]
                    # print(result)
                    if len(result) > 0:
                        for res in result:
                            if int(res) in range(start-1,end+2):
                                clear_post = False  

                if not clear_pre or not clear_post:
                    # print("FOUND: " + ele  + " START: " + str(start) + " END: " + str(end))
                    printSameLine(colored(ele, 'cyan'))
                    
                    parts.append(ele)
                    # parts.remove(ele)
                else:
                    printSameLine(colored(ele, 'red'))

            else:
                # print(ele)
                if ele not in symbols:
                    # print(ele)
                    for char in ele:
                        if char in symbols:
                            for num in ele.split(char):
                                if num != '':
                                    # print("NUM: " + num)
                                    parts.append(num)
                    start = line.find(ele)
                    printSameLine(line[printIndex:start])
                    printIndex = start + len(ele)
                    printSameLine(colored(ele, 'yellow'))

                # else:
                #     start = line.find(ele)
                #     printSameLine(line[printIndex:start])
                #     printIndex = start +1
                #     printSameLine(colored(ele, 'green'))
    printSameLine(line[printIndex:])
    # sys.exit()
                    
                    

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