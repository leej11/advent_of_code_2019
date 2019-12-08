instructions = ['R8','U5','L5','D3']
instructions2 = ['U7', 'R6', 'D4', 'L4']

instructions3 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
instructions4 = ['U62','R66','U55','R34','D71','R55','D58','R83']


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
