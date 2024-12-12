import re
from day3_part1 import parse_input



def main(input):

    pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"

    matches = re.findall(pattern, input)

    filtered = []

    status = True

    s = 0

    for x in matches:
        if x == "don't()":
            status = False
        elif x == "do()":
            status = True
            continue
        
        if status:
            y = x.replace("mul(","").replace(")","").split(",")
            s = (int(y[0])*int(y[1]))
            filtered.append(s)

    calc(filtered)

def calc(input):
    result = 0
    for num in input:
        result += num
    
    print(result)



if __name__ == "__main__":
    input = parse_input()
    main(input)