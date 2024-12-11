from day2_part1 import parseInput, increaseCheck 


def rule1(input):
    increase = increaseCheck(input)
    control = input[0]
    for num in input:
        match increase:
            case True:
                if num < control:
                    return False
                else:
                    control = num
            
            case False:
                if num > control:
                    return False
                else:
                    control = num
    return rule2(input)



def rule2(input):
    increase = increaseCheck(input)
    for i in range(len(input) - 1):
        match increase:
            case True:
                if (input[i] - input[i + 1]) * -1 > 3 or (input[i] - input[i + 1]) * -1 < 1:
                    return False
            case False:
                if input[i] - input[i + 1] > 3 or input[i] - input[i + 1] < 1:
                    return False
    return True



def check_report(input):
    precheck = rule1(input)
    if precheck:
        return True

    for i in range(len(input)):
        templist = input.copy()
        templist.pop(i)
        result = rule1(templist)
        if result == True:
            return True
        
    return False
            


def main(input):
    safe = 0
    for report in input:
        result = check_report(report)
        if result:
            safe += 1

    print(safe)          
    
    




if __name__ == "__main__":
    input = parseInput()
    main(input)