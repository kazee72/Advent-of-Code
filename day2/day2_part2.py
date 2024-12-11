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
            
    return True



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
    for num in input:
        templist = input
        templist.remove(num)
        result = rule1(templist)
        if result == False:
            return False
    return True
            


def main(input):
    safe = 0
    for report in input:
        result = check_report(report)
        if result == True:
            safe += 1

    print(safe)          
    
    




if __name__ == "__main__":
    input = parseInput()
    main(input)