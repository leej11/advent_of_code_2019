# 1202 Program Alarm
# An intcode program
# First Number: "Opcode" [1,2,99], indicates what to do

test_list = [3,9,8,9,10,9,4,9,99,-1,8]

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

        ######## Opcode 5 ########
        # Jump-if-true. If first parameter != 0, instruction pointer set to the value from
        # the second parameter, otherwise nothing

        elif str(test_list[x])[-1:] == '5':
            pass

        ######## Opcode 6 ########
        # Jump-if-false. If first parameter == 0, instruction pointer set to the value from
        # the second parameter, otherwise nothing

        elif str(test_list[x])[-1:] == '6':
        pass

        ######## Opcode 7 ########
        # Less-than. If first parameter < second parameter, stores value = 1 in position of 3rd parameter
        # Otherwise, value = 0

        elif str(test_list[x])[-1:] == '7':
        pass

        ######## Opcode 8 ########
        # Equals. If first parameter == second parameter, stores value = 1 in position of 3rd parameter

        elif str(test_list[x])[-1:] == '8':
        pass



        # Opcode 99 means just do nothing except increase along the list of numbers
        elif str(test_list[x])[-2:] == '99':
            break

        # Error in case I've missed something
        else:
            print("Error")
            break


intcode_computer(1,test_list)