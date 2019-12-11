# 1202 Program Alarm
# An intcode program
# First Number: "Opcode" [1,2,99], indicates what to do

test_list = [1002,4,3,4,33]

x = 0

def intcode_computer(test_list):

    # This while loop performs the value re-assignment described in the challenge
    while x < len(test_list) - 1:

        # Opcode 1 means sum the following 2 numbers and reassign to the location of the
        # 3rd number
        if str(test_list[x])[-2:] == 01:

            # Parameter 1
            # Immediate mode
            if str(test_list[x])[-3] == 1:
                param1 = test_list[x + 1]

            # Position mode
            else:
                param1 = test_list[test_list[x + 1]]


            # Parameter 2
            # Immediate mode
            if str(test_list[x])[-4] == 1:
                param2 = test_list[x + 2]

            # Position mode
            else:
                param2 = test_list[test_list[x + 2]]


            # Parameter 3
            # Immediate mode
            if str(test_list[x])[-5] == 1:
                param3 = test_list[x + 3]

            # Position mode
            else:
                param3 = test_list[test_list[x + 3]]

        value = param1 + param2
        test_list[param3] = value
        x += 4



        # Opcode 2 means multiple the following 2 numbers and reassign to the location of the
        # 3rd number
        elif str(test_list[x])[-2:] == 02:
            value = test_list[test_list[x+1]] * test_list[test_list[x+2]]
            test_list[test_list[x+3]] = value
            print("x = 2 done, now increasing by 4")
            x += 4
            print("{}".format(x))

        # Opcode 3 - Take a single integer as an input and save to the position given by that number
        elif str(test_list[x])[-2:] == 03:
            value = test_list[x+1]
            test_list[test_list[x+1]] = value
            x += 2

        # Opcode 4 - Output the value of the position of the parameter
        elif str(test_list[x])[-2:] == 04:
            value = test_list[x+1]
            output = test_list[value]
            x += 2

        # Opcode 99 means just do nothing except increase along the list of numbers
        elif str(test_list[x])[-2:] == 99:
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

