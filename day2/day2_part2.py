from day2_part1 import parseInput, increaseCheck 


def rule1(input, tolerance):
    increase = increaseCheck(input)
    control = input[0]
    for num in input:
        match increase:
            case True:
                if num < control:
                    if tolerance == 0:
                        return False
                    else:
                        tolerance = 0
                        input.remove(num)
                        rule1(input, tolerance)
                else:
                    control = num
            
            case False:
                if num > control:
                    if tolerance == 0:
                        return False
                    else:
                        tolerance = 0
                        input.remove(num)
                        rule1(input, tolerance)
                else:
                    control = num
            
    result = rule2(input, tolerance)
    return result



def rule2(input, tolerance):
    increase = increaseCheck(input)
    i = 0
    while i < len(input) - 1:
        if increase:
            if (input[i] - input[i + 1]) * -1 > 3 or (input[i] - input[i + 1]) * -1 < 1:
                if tolerance == 0:
                    return False
                else:
                    tolerance = 0
                    input.remove(input[i])

        else:
            if input[i] - input[i + 1] > 3 or input[i] - input[i + 1] < 1:
                if tolerance == 0:
                    return False
                else:
                    tolerance = 0
                    input.remove(input[i])
        
        i += 1

    return True




def main(input):
    safe = 0
    tolerance = 1
    for report in input:
        result = rule1(report, tolerance)
        if result == True:
            safe += 1

    print(safe)            
    
    




if __name__ == "__main__":
    input = parseInput()
    main(input)