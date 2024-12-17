from day5_part1 import parse_input



def check(rules, update):
    for rule in rules:
        if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
            return update.index(rule[0]), update.index(rule[1])
    return True



def switch(update, indices):
    temp = [update[indices[0]], update[indices[1]]]
    update[indices[0]] = temp[1]
    update[indices[1]] = temp[0]

    return update



def main(input):
    rules = input[0]
    updates = input[1]

    values = []
    
    for update in updates:
        switched = False
        check_result = check(rules, update)
        while check_result != True:
            update = switch(update, check_result)
            check_result = check(rules, update)
            switched = True
        
        if switched:
            values.append(update[len(update)// 2])

    print(values)
        
    result = 0
    for value in values:
        result += int(value)

    print(result)

    

if __name__ == "__main__":
    input = parse_input()
    main(input)