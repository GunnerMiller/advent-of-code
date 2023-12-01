def checkForNumberSpelledForward(string, index):
    try:
        if(string[index] == "o"):
            if(string[index+1] != "n"):
                    return -1  
            if(string[index+2] != "e"):
                    return -1
            return 1
                       
        elif(string[index] == "t"):
            if(string[index+1] == "w"):
                if(string[index+2] == "o"):
                    return 2
            if(string[index+1] == "h"):
                if(string[index+2] != "r"):
                    return -1
                if(string[index+3] != "e"):
                    return -1
                if(string[index+4] != "e"):
                    return -1
                return 3
            
        elif(string[index] == "f"):
            if(string[index+1] == "o"):
                if(string[index+2] != "u"):
                    return -1
                if(string[index+3] != "r"):
                    return -1
                return 4
            if(string[index+1] == "i"):
                if(string[index+2] != "v"):
                    return -1
                if(string[index+3] != "e"):
                    return -1
                return 5

        elif(string[index] == "s"):
            if(string[index+1] == "i"):
                if(string[index+2] != "x"):
                    return -1
                return 6
            if(string[index+1] == "e"):
                if(string[index+2] != "v"):
                    return -1
                if(string[index+3] != "e"):
                    return -1
                if(string[index+4] != "n"):
                    return -1
                return 7
            
        elif(string[index] == "e"):
            if(string[index+1] != "i"):
                    return -1  
            if(string[index+2] != "g"):
                    return -1
            if(string[index+3] != "h"):
                    return -1  
            if(string[index+4] != "t"):
                    return -1
            return 8
            
        elif(string[index] == "n"):
            if(string[index+1] != "i"):
                    return -1  
            if(string[index+2] != "n"):
                    return -1
            if(string[index+3] != "e"):
                    return -1  
            return 9
    except:
        return -1
    
    ##IDFK
    return -1

def checkForNumberSpelledBackward(string, index):
    try:
        if(string[index]) == "e":
            if(string[index-1]== "n"):
                if(string[index-2]== "o"):
                    return 1
                if(string[index-2]== "i"):
                    if(string[index-3]== "n"):
                        return 9
            if(string[index-1]== "v"):
                if(string[index-2] != "i"):
                    return -1
                if(string[index-3] != "f"):
                    return -1
                return 5
            if(string[index-1]== "e"):
                if(string[index-2] != "r"):
                    return -1
                if(string[index-3] != "h"):
                    return -1
                if(string[index-4] != "t"):
                    return -1
                return 3
        
        if(string[index]) == "o":
            if(string[index-1] != "w"):
                return -1
            if(string[index-2] != "t"):
                return -1
            return 2
        
        if(string[index]) == "r":
            if(string[index-1] != "u"):
                return -1
            if(string[index-2] != "o"):
                return -1
            if(string[index-3] != "f"):
                return -1
            return 4
        
        if(string[index]) == "n":
            if(string[index-1] != "e"):
                return -1
            if(string[index-2] != "v"):
                return -1
            if(string[index-3] != "e"):
                return -1
            if(string[index-4] != "s"):
                return -1
            return 7
        
        if(string[index]) == "x":
            if(string[index-1] != "i"):
                return -1
            if(string[index-2] != "s"):
                return -1
            return 6
        
        if(string[index]) == "t":
            if(string[index-1] != "h"):
                return -1
            if(string[index-2] != "g"):
                return -1
            if(string[index-3] != "i"):
                return -1
            if(string[index-4] != "e"):
                return -1
            return 8
    except:
        print("EXCEPTION!!!")
        return -1
    
    ##IDFK
    return -1

def main():
    file = open("input.txt", "r")
    content = file.read()
    inputs = content.split('\n')
    sum = 0
    for ele in inputs:
        ### TESTING ###
        # ele = "21three"
        ### TESTING ###
        
        # Tens place, iterate from the front
        for i in range(len(ele)):
            value = checkForNumberSpelledForward(ele, i)
            if (value > 0):
                sum = sum +(value * 10)
                break
            elif (ele[i].isnumeric()):
                sum = sum + int(ele[i]) * 10
                break
        # Ones place, iterate from the end
        for i in reversed(range(len(ele))):
            value = checkForNumberSpelledBackward(ele, i)
            print(value)
            if (value > 0):
                sum = sum + value
                break
            elif(ele[i].isnumeric()):
                sum = sum + int(ele[i])
                break 
        
        ### TESTING ###
        # break
        ### TESTING ###
    print(sum)

if __name__=="__main__":
   main()