number_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

file = open("input.txt", "r")
content = file.read()
inputs = content.split('\n')
sum1 = 0
sum2 = 0
for ele in inputs:      
    part_one_digits = []
    part_two_digits = []

    for i, char in enumerate(ele):
        if (char.isdigit()):
            part_one_digits.append(char)
            part_two_digits.append(char)
        else:
            for index, value in enumerate(number_strings):
                if( ele[i:].startswith(value) ):
                    part_two_digits.append(str(index+1))
    
    sum1 += int(part_one_digits[0] + part_one_digits[-1])
    sum2 += int(part_two_digits[0] + part_two_digits[-1])
        
print(sum1)
print(sum2)