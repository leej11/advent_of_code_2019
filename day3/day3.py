instructions = ['R8','U5','L5','D3']
instructions2 = ['U7', 'R6', 'D4', 'L4']


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

    for item in intersections:
        sum(item)
