from day2_part1 import parseInput, increaseCheck 


def rule1(input):
    increase = increaseCheck(input)
    tolerance = 1
    control = input[0]
    for num in input:
        match increase:
            case True:
                if num < control:
                    if tolerance == 0:
                        return False
                    else:
                        tolerance = 0
                        control = num
                else:
                    control = num
            
            case False:
                if num > control:
                    if tolerance == 0:
                        return False
                    else:
                        tolerance = 0
                        control = num
                else:
                    control = num
            
    result = rule2(input, tolerance)
    return result



def rule2(input, tolerance):
    increase = increaseCheck(input)
    for i in range(len(input) - 1):
        match increase:
            case True:
                if (input[i] - input[i + 1]) * -1 > 3 or (input[i] - input[i + 1]) * -1 < 1:
                    if tolerance == 0:
                        return False
                    else:
                        tolerance = 0
            case False:
                if input[i] - input[i + 1] > 3 or input[i] - input[i + 1] < 1:
                    if tolerance == 0:
                        return False
                    else:
                        tolerance = 0
    return True




def main(input):
    safe = 0
    for report in input:
        result = rule1(report)
        if result == True:
            safe += 1

    print(safe)            
    
    




if __name__ == "__main__":
    input = parseInput()
    main(input)