import re



def parse_input():
    input = ""
    with open("day3_input.txt", "r") as file:
        for line in file:
            input += line
    return input



def calc(input):
    total = 0
    for tuple in input:
        total += int(tuple[0]) * int(tuple[1])

    print(total)
            


def main(input):
    total = 0
    pattern = r"mul\((-?\d{1,3}),(-?\d{1,3})\)"
    matches = re.findall(pattern, input)

    calc(matches)



if __name__ == "__main__":
    input = parse_input()
    main(input)