import datetime
start = datetime.datetime.now()

inputs = open("5.txt", "r").readlines()
curr_lowest = None
seeds = inputs[0].split(":")[1].strip().split()
for x in range(0, len(seeds), 2):
    i = 1
    values = {int(seeds[x]) : int(seeds[x]) + int(seeds[x+1]) - 1}
    while i < len(inputs):
        line = inputs[i]
        if line != "\n": 
            if not line[0].isdigit():
                transformed = {}
                while i+1 < len(inputs) and inputs[i+1][0].isdigit():
                    dest, source, range_length = inputs[i+1].split()
                    ruleStart = int(source)
                    ruleEnd = ruleStart + int(range_length) - 1
                    t_factor = int(dest) - int(source) # amount to transform by
                    
                    stack = list(values.keys())
                    while len(stack) > 0:
                        key = stack.pop()
                        valueStart = int(key)
                        valueEnd = int(values[key])
                        if valueStart >= ruleStart and valueEnd <= ruleEnd:
                            del values[key]
                            transformed[valueStart + t_factor] = valueEnd + t_factor
                        elif ruleStart >= valueStart and ruleEnd <= valueEnd:
                            del values[key]
                            transformed[ruleStart + t_factor] = ruleEnd + t_factor
                            values[valueStart] = ruleStart - 1
                            stack.append(valueStart)
                            values[ruleEnd + 1] = valueEnd
                            stack.append(ruleEnd + 1)
                        elif ruleStart >= valueStart and ruleStart <= valueEnd:
                            del values[key]
                            transformed[ruleStart + t_factor] = valueEnd = t_factor
                            values[valueStart] = ruleStart - 1
                            stack.append(valueStart)
                        elif ruleEnd >= valueStart and ruleEnd <= valueEnd:
                            del values[key] 
                            transformed[valueStart + t_factor] = ruleEnd + t_factor
                            values[ruleEnd + 1] = valueEnd
                            stack.append(ruleEnd + 1)
                    i+=1
                for ele in transformed.keys():
                    values[ele] = transformed[ele]
        i+=1
    temp = list(values.keys())
    temp.sort()
    curr_low = temp[0]
    curr_lowest = curr_low if curr_lowest == None else min(curr_lowest, curr_low)
    
end = datetime.datetime.now()
result = end - start
print("RUNTIME=" + str(result.total_seconds()) + " sec")
print("RUNTIME=" + str(result.total_seconds() * 1000) + " ms")
print(curr_lowest)