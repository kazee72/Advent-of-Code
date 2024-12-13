


def parse_input():
    input = ""
    with open("day4_input.txt", "r") as file:
        for line in file:
            line = line.rstrip("\n")
            input += line

    return input



def check_xmas(input):
    total = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "X":
                hor = horizontal(i, j, input)
                vert = vertical(i, j, input)
                diag = diagonal(i, j, input)
                total += hor + vert + diag
            else:
                continue
    
    return total



def horizontal(i, j, input):
    counter = 0
    print(i, j)
    if len(input[i]) > j + 3:
        if input[i][j + 1] == "M" and input[i][j + 2] == "A" and input[i][j + 3] == "S":
            counter += 1

    if 0 >= j - 3:
        if input[i][j - 1] == "M" and input[i][j - 2] == "A" and input[i][j - 3] == "S":
            counter += 1

    return counter
    


def vertical(i, j, input):
    counter = 0
    if len(input) > i + 3:
        if input[i + 1][j] == "M" and input[i + 2][j] == "A" and input[i + 3][j] == "S":
            counter += 1

    if 0 <= i - 3:
        if input[i - 1][j] == "M" and input[i - 2][j] == "A" and input[i - 3][j] == "S":
            counter += 1

    return counter



def diagonal(i, j, input):
    counter = 0
    if 0 <= i - 3 and 0 <= j - 3:
        if input[i - 1][j - 1] == "M" and input[i - 2][j - 2] == "A" and input[i - 3][j - 3] == "S":
            counter += 1

    if 0 <= j - 3 and len(input[i]) < i + 3:
        if input[i + 1][j - 1] == "M" and input[i + 2][j - 2] == "A" and input[i + 3][j - 3] == "S":
            counter += 1

    if 0 <= i - 3 and len(input) < j + 3:
        if input[i - 1][j + 1] == "M" and input[i - 2][j + 2] == "A" and input[i - 3][j + 3] == "S":
            counter += 1

    if len(input[i]) < i + 3 and len(input) < j + 3:
        if input[i + 1][j + 1] == "M" and input[i + 2][j + 2] == "A" and input[i + 3][j + 3] == "S":
            counter += 1        

    return counter


def main(input):
    result = check_xmas(input)
    print(result)



if __name__ == "__main__":
    input = parse_input()
    main(input)
