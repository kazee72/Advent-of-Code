from day1_part1 import getInput



def main(input):
    similarity_score = 0
    similarities = []
    for num_list1 in input[0]:
        counter = 0
        for num_list2 in input[1]:
            if num_list1 == num_list2:
                counter += 1
        similarities.append(num_list1 * counter)
    
    for score in similarities:
        similarity_score += score
    
    print(similarity_score)
            


if __name__ == "__main__":
    input = getInput()
    main(input)