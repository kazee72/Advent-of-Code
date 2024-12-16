


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



def includes(rule, update):
    counter = 0
    for num in rule:
        if num in update:
            counter += 1
        
    return counter == 2
    
        

def check_rule(rule, update):
    return update.index(rule[0]) < update.index(rule[1])



def main(input):
    rules = input[0]
    updates = input[1]

    for update in updates:
        counter = 0
        for rule in rules:
            include = includes(rule, update)
            if include:
                pass_rule = check_rule(rule, update)
                if pass_rule:
                    counter += 1
                else:
                    break
            if counter == len(rules):
                print("Rule ", rules.index(rule), " passes")




if __name__ == "__main__":
    input = parse_input()
    main(input)