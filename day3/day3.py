input_instructions = ['R8','U5','L5','D3']
start_loc = [1,1]
grid = [4,4]

def create_grid(gridspec):
    print("Creating grid...")
    grid = [[0 for i in range(gridspec[1])] for j in range(gridspec[0])]
    for row in grid:
        print(row)

    return grid

def print_grid(grid):
    print("Printing grid...")
    for row in grid:
        print(row)

test_instructions = ['R4', 'U4']


def move_route(instructions):

    gridspec = [4,4]
    my_grid = create_grid(gridspec)
    start_loc = [gridspec[0]-1, 0]

    for item in instructions:

        if item[0] == 'R':
            print("Moving right {} spaces".format(item[1:]))

            # Log route taken with 1s
            for i in range(int(item[1:])):
                my_grid[start_loc[0]][i] = 1

            # Update current position
            start_loc[1] = start_loc[1] + int(item[1:])-1
            print("New x position of {}".format(start_loc[1]))





        elif item[0] == 'U':
            print("Moving up {} spaces".format(item[1:]))

            # Log route taken with 1s
            for i in range(int(item[1:])):
                my_grid[start_loc[0] - i][start_loc[1]] = 1

            # Update current position
            start_loc[1] = start_loc[1] + int(item[1:])
            print("New y position of {}".format(start_loc[1]))

        # elif item[0] == 'D':
        #     start_loc[1] = start_loc[1] - int(item[1:])

        else:
            print("Error")


    print_grid(my_grid)

move_route(test_instructions)