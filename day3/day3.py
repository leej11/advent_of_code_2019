def read_input(filename)

    # Read the input file
    input_file = open(filename, 'r')

    # Clear and new lines and split up commands
    instruction_lists = [line.strip('\n').split(',') for line in input_instructions]

    # Map the separate instruction lists to 2 separate lists
    instructions1, instructions2 = map(list, zip(*instruction_lists))

    # input_instructions = open('day3/input.txt', 'r')
    # instructions = [line.strip('\n').split(',') for line in input_instructions]

    return instructions1, instructions2



def traverse_route(instructions):

    curr_coords = (0,0)
    traversed_coords = []

    for instruction in instructions:

        # Traverse right
        if instruction[0] == 'R':

            for i in range(int(instruction[1:])):
                traversed = (curr_coords[0] + (i+1), curr_coords[1])
                traversed_coords.append(traversed)

            curr_coords = (curr_coords[0] + int(instruction[1:]), curr_coords[1])

        # Traverse left
        elif instruction[0] == 'L':

            for i in range(int(instruction[1:])):
                traversed = (curr_coords[0] - (i + 1), curr_coords[1])
                traversed_coords.append(traversed)

            curr_coords = (curr_coords[0] - int(instruction[1:]), curr_coords[1])

        # Traverse up
        if instruction[0] == 'U':

            for i in range(int(instruction[1:])):
                traversed = (curr_coords[0], curr_coords[1] + (i + 1))
                traversed_coords.append(traversed)

            curr_coords = (curr_coords[0], curr_coords[1] + int(instruction[1:]))

        # Traverse left
        elif instruction[0] == 'D':

            for i in range(int(instruction[1:])):
                traversed = (curr_coords[0], curr_coords[1] - (i + 1))
                traversed_coords.append(traversed)

            curr_coords = (curr_coords[0], curr_coords[1] - int(instruction[1:]))

    return traversed_coords


route1 = traverse_route(instructions)
route2 = traverse_route(instructions2)
route3 = traverse_route(instructions3)
route4 = traverse_route(instructions4)



def get_shortest_intersect(route1, route2):

    intersections = set(route1) & set(route2)
    abs_intersections = [(abs(i[0]), abs(i[1])) for i in intersections]

    return print(sum(min(abs_intersections, key=sum)))

get_shortest_intersect(route1,route2)
get_shortest_intersect(route3,route4)
