


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
                temp.append(int(line[1:2]))
                temp.append(int(line[4:]))
                rules.append(temp)
            else:
                for num in line:
                    if num == ",":
                        continue
                    temp.append(int(num))
                updates.append(temp)

    return rules, updates 




    
        

def check(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
            return False
    return True



def main(input):
    rules = input[0]
    updates = input[1]

    results = []

    for update in updates:
        result = check(rules, update)
        results.append(result)

    print(results)





if __name__ == "__main__":
    input = parse_input()
    main(input)