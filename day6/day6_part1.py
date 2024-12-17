import sys
sys.setrecursionlimit(15000)



def parse_input():
    input = []

    with open("day6_input.txt", "r") as file:
        for line in file:
            line = line.strip("\n")
            input.append(list(line))
        
    return input



def search_start(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "^":
                return [i, j]
            
        

def move(input, pos, guard, dist_pos):
    dist_pos.append(pos.copy())
    
    try:
        match guard:
            case "^":
                if input[pos[0] - 1][pos[1]] == "#":
                    guard = ">"
                else:
                    pos[0] -= 1
                    
            case "<":
                if input[pos[0]][pos[1] - 1] == "#":
                    guard = "^"
                else:
                    pos[1] -= 1

            case ">":
                if input[pos[0]][pos[1] + 1] == "#":
                    guard = "v"
                else:
                    pos[1] += 1

            case "v":
                if input[pos[0] + 1][pos[1]] == "#":
                    guard = "<"
                else:
                    pos[0] += 1

        input[pos[0]][pos[1]] = guard
        return move(input, pos, guard, dist_pos)
    except IndexError:
        return dist_pos
    


def count_dist_pos(positions):
    distinct = []
    for pos in positions:
        if pos in distinct:
            continue
        else:
            distinct.append(pos)
        
    return len(distinct)



def main(input):
    start = search_start(input)
    distinct_positions = []
    positions = move(input, start, "^", distinct_positions)

    result = count_dist_pos(positions)

    print(result)




if __name__ == "__main__":
    input = parse_input()
    main(input)