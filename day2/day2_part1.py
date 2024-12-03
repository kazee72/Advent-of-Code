


def parseInput():
    reports = []
    with open("day2_input.txt", "r") as file:
        for line in file:
            line = line.replace("\n", "")
            reports.append([line])

    reports = [list(map(int, sublist[0].split())) for sublist in reports]

    return reports



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
                
    

def increaseCheck(input):
    if input[0] < input[1]:
        return True
    else:
        return False



def main(input):
    safe = 0
    for report in input:
        result1 = rule1(report)
        result2 = rule2(report)

        if result1 and result2 == True: 
            safe += 1
    
    print(safe)
    


if __name__ == "__main__":
    input = parseInput()
    main(input)