def read_input(filename):

    # Read the input file
    input_file = open(filename, 'r')

    # Clear and new lines and split up commands
    instruction_lists = [line.strip('\n').split(',') for line in input_file]

    # Map the separate instruction lists to 2 separate lists
    instructions1, instructions2 = instruction_lists[0], instruction_lists[1]

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



def get_shortest_intersect(route1, route2):

    intersections = set(route1) & set(route2)
    abs_intersections = [(abs(i[0]), abs(i[1])) for i in intersections]

    # return print(sum(min(abs_intersections, key=sum)))
    return intersections


def get_wires_to_intersect(intersections, route1, route2):

        rt1_indices = [(num, tupl) for num, tupl in enumerate(route1) if tupl in intersections]
        rt2_indices = [(num, tupl) for num, tupl in enumerate(route2) if tupl in intersections]
        route_sums = []

        for num, tupl in enumerate(route1):

            if tupl in intersections:

                for num2, tupl2 in enumerate(route2):

                    if tupl == tupl2:

                        print("{} - {} and {} - {}".format(num, tupl, num2, tupl2))
                        route_sums.append((num+num2 + 2, tupl))

        return min(route_sums)[0]



instructions1, instructions2 = read_input('input.txt')
route1 = traverse_route(instructions1)
route2 = traverse_route(instructions2)
intersections = get_shortest_intersect(route1, route2)
# get_shortest_intersect(route1, route2)

test = get_wires_to_intersect(intersections, route1, route2)
print(test)
