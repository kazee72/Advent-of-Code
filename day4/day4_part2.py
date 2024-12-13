from day4_part1 import parse_input




def check_cross(i, j, input):
    counter = 0
    if 0 <= i - 1 and 0 <= j - 1 and len(input[i]) > i + 1 and len(input) > j + 1:
        if (input[i - 1][j - 1] == "M" and input[i + 1][j + 1] == "S") or (input[i - 1][j - 1] == "S" and input[i + 1][j + 1] == "M"):
            counter += 1
    if 0 <= i - 1 and len(input) > j + 1 and len(input[i]) > i + 1 and 0 <= j - 1:
        if (input[i - 1][j + 1] == "M" and input[i + 1][j - 1] == "S") or (input[i - 1][j + 1] == "S" and input[i + 1][j - 1] == "M"):
            counter += 1
    
    if counter == 2:
        return 1
    else:
        return 0


def main(input):
    result = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "A":
                result += check_cross(i, j, input)

    print(result)




if __name__ == "__main__":
    input = parse_input()
    main(input)