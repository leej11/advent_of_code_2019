# 1202 Program Alarm
# An intcode program
# First Number: "Opcode" [1,2,99], indicates what to do

test_list = [3,225,1,225,6,6,1100,1,238,225,104,0,2,218,57,224,101,-3828,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,26,25,224,1001,224,-650,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1102,44,37,225,1102,51,26,225,1102,70,94,225,1002,188,7,224,1001,224,-70,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,86,70,225,1101,80,25,224,101,-105,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,101,6,91,224,1001,224,-92,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,61,60,225,1001,139,81,224,101,-142,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,102,40,65,224,1001,224,-2800,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1102,72,10,225,1101,71,21,225,1,62,192,224,1001,224,-47,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1101,76,87,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,374,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,107,677,226,224,102,2,223,223,1006,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1107,677,677,224,1002,223,2,223,1006,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,449,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1006,224,554,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,644,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]

def intcode_computer(input, test_list):

    x = 0

    # This while loop performs the value re-assignment described in the challenge
    while x < len(test_list) - 1:

        ######## Opcode 1 ########
        # Sum the following 2 numbers and reassign to the location of the
        # 3rd number

        if str(test_list[x])[-1:] == '1':

            print("Starting opcode {} at position {}".format(str(test_list[x]),x))
            # Corresponds to 00001
            if len(str(test_list[x])) == 1:
                param1 = test_list[test_list[x + 1]]
                param2 = test_list[test_list[x + 2]]

            # Corresponds to 00101
            elif len(str(test_list[x])) == 3:
                param1 = test_list[x + 1]
                param2 = test_list[test_list[x + 2]]

            # Corresponds to 01001 or 01101
            elif len(str(test_list[x])) == 4:

                if str(test_list[x])[1] == '1':
                    param1 = test_list[x + 1]
                    param2 = test_list[x + 2]

                elif str(test_list[x])[1] == '0':
                    param1 = test_list[test_list[x + 1]]
                    param2 = test_list[x + 2]


            param3 = test_list[x + 3]

            value = param1 + param2
            test_list[param3] = value

            print("Completed opcode {} at position {}".format(str(test_list[x]), x))
            x += 4


        ######## Opcode 2 ########
        # Multiply the following 2 numbers and reassign to the location of the
        # 3rd number
        elif str(test_list[x])[-1:] == '2':

            print("Starting opcode {} at position {}".format(str(test_list[x]), x))
            # Corresponds to 00001
            if len(str(test_list[x])) == 1:
                param1 = test_list[test_list[x + 1]]
                param2 = test_list[test_list[x + 2]]

            # Corresponds to 00101
            elif len(str(test_list[x])) == 3:
                param1 = test_list[x + 1]
                param2 = test_list[test_list[x + 2]]

            # Corresponds to 01001 or 01101
            elif len(str(test_list[x])) == 4:

                if str(test_list[x])[1] == '1':
                    param1 = test_list[x + 1]
                    param2 = test_list[x + 2]

                elif str(test_list[x])[1] == '0':
                    param1 = test_list[test_list[x + 1]]
                    param2 = test_list[x + 2]

            param3 = test_list[x + 3]6069343

            value = param1 * param2
            test_list[param3] = value

            print("Completed opcode {} at position {}".format(str(test_list[x]), x))
            x += 4


        ######## Opcode 3 ########
        # Take a single integer as an input and save to the position given by that number

        elif str(test_list[x])[-1:] == '3':
            print("Starting opcode {} at position {}".format(str(test_list[x]), x))

            test_list[test_list[x+1]] = input

            print("Completed opcode {} at position {}".format(str(test_list[x]), x))
            x += 2



        ######## Opcode 4 ########
        # Output the value of the position of the parameter

        elif str(test_list[x])[-1:] == '4':
            print("Starting opcode {} at position {}".format(str(test_list[x]), x))
            value = test_list[test_list[x+1]]

            # Corresponds to 00004
            if len(str(test_list[x])) == 1:
                value = test_list[test_list[x+1]]

            # Corresponds to 00104
            elif len(str(test_list[x])) > 1:
                value = test_list[x+1]

            if value != 0:
                print(value)
                print(test_list)

            else:
                print(value)

            x += 2

            print("Completed opcode {} at position {}".format(str(test_list[x]), x))

        # Opcode 99 means just do nothing except increase along the list of numbers
        elif str(test_list[x])[-2:] == '99':
            break

        # Error in case I've missed something
        else:
            print("Error")
            break


intcode_computer(1,test_list)