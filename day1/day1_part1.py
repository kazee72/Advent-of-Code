


def getInput():
    left_numbers = []
    right_numbers = []
    with open('day1/day1_input.txt', 'r') as file: 
        # split lines into 2 nums
        for line in file: 
            left, right = line.split() 
            left_numbers.append(int(left)) 
            right_numbers.append(int(right))

    input = []
    input.append(left_numbers)
    input.append(right_numbers)

    return input



def main(input):
    differences = []
    input_sorted = []
    total_distance = 0

    # sort lists
    for list in input:
        list.sort()
        input_sorted.append(list)

    list1, list2 = input_sorted

    # get differences
    for i in range(len(list1)):
        diff = list1[i] - list2[i]
        diff = diff * -1 if diff < 0 else diff
        differences.append(diff)

    for difference in differences:
        total_distance += difference
        
    print(total_distance)



if __name__ == "__main__":
    input = getInput()
    main(input)