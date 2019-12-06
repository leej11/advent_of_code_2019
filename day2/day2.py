# 1202 Program Alarm
# An intcode program
# First Number: "Opcode" [1,2,99], indicates what to do

import itertools

# Create list of possible values for address 1 and 2 for part 2
pre_list1 = list(range(0,100))
pre_list2 = list(range(0,100))
my_list = pre_list1 + pre_list2
my_tuples_list = []

for pair in itertools.combinations(my_list,2):
    my_tuples_list.append(pair)



for (i, j) in my_tuples_list:
    test_list = [1,i,j,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,1,6,23,27,1,10,27,31,1,5,31,35,2,6,35,39,1,5,39,43,1,5,43,47,2,47,6,51,1,51,5,55,1,13,55,59,2,9,59,63,1,5,63,67,2,67,9,71,1,5,71,75,2,10,75,79,1,6,79,83,1,13,83,87,1,10,87,91,1,91,5,95,2,95,10,99,2,9,99,103,1,103,6,107,1,107,10,111,2,111,10,115,1,115,6,119,2,119,9,123,1,123,6,127,2,127,10,131,1,131,6,135,2,6,135,139,1,139,5,143,1,9,143,147,1,13,147,151,1,2,151,155,1,10,155,0,99,2,14,0,0]

    x = 0

    # This while loop performs the value re-assignment described in the challenge
    while x < len(test_list) - 1:

        # Opcode 1 means sum the following 2 numbers and reassign to the location of the
        # 3rd number
        if test_list[x] == 1:
            value = test_list[test_list[x+1]] + test_list[test_list[x+2]]
            test_list[test_list[x+3]] = value
            print("x = 1 done, now increasing by 4")
            x+=4
            print("{}".format(x))

        # Opcode 2 means multiple the following 2 numbers and reassign to the location of the
        # 3rd number
        elif test_list[x] == 2:
            value = test_list[test_list[x+1]] * test_list[test_list[x+2]]
            test_list[test_list[x+3]] = value
            print("x = 2 done, now increasing by 4")
            x += 4
            print("{}".format(x))

        # Opcode 99 means just do nothing except increase along the list of numbers
        elif test_list[x] == 99:
            print("code 99, increasing by 4")
            x += 4
            print("{}".format(x))

        # Error in case I've missed something
        else:
            print("Error")

    # This is the solution we're looking for
    if test_list[0] == 19690720:
        print("Found it, the pair is {} and {}".format(test_list[1], test_list[2]))
        break

    else:
        print("Not found the pair yet")

