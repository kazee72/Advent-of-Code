


def parse_input():
    rules = []
    updates = []
    switch = False

    with open("day5_input.txt", "r") as file:
        for line in file:
            temp = []
            if line == "\n":
                switch = True
                continue
            
            line = line.strip("\n")
            
            if not switch:
                temp.append(line[0:2])
                temp.append(line[3:])
                rules.append(temp)
            else:
                line = line.split(",")
                updates.append(line)

    return rules, updates 



def check(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
            return False
    return update



def calc(input):
    result = 0
    for update in input:
        result += int(update[len(update) // 2])

    return result



def main(input):
    rules = input[0]
    updates = input[1]

    passed_updates = []

    for update in updates:
        result = check(rules, update)
        if result:
            passed_updates.append(result)

    answer = calc(passed_updates)
    print(answer)



if __name__ == "__main__":
    input = parse_input()
    main(input)