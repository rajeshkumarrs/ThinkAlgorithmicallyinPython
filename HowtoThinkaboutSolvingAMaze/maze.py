maze_str = """
    * * * * * * * * * * * * *
    *           *           *
    * * *   *   * * * * *   *
    *       *           *   *
    *   * * * *         *   *
    o   *     *         *   *
    * * * * * * * * *       *
    *               *       *
    *   *   * * *   * * *   *
    *   *       * * *       *
    *   *               * * *
    *   * * * *             *
    *         *             *
    * * * * x * * * * * * * *
    """
# print(maze_str)
maze_lst = [
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", " ", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", "*"],
    ["*", "*", "*", " ", "*", " ", "*", "*", "*", "*", "*", " ", "*"],
    ["*", " ", " ", " ", "*", " ", " ", " ", " ", " ", "*", " ", "*"],
    ["*", " ", "*", "*", "*", "*", " ", " ", " ", " ", "*", " ", "*"],
    ["o", " ", "*", " ", " ", "*", " ", " ", " ", " ", "*", " ", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", " ", " ", " ", " ", "*", " ", " ", " ", "*"],
    ["*", " ", "*", " ", "*", "*", "*", " ", "*", "*", "*", " ", "*"],
    ["*", " ", "*", " ", " ", " ", "*", "*", "*", " ", " ", " ", "*"],
    ["*", " ", "*", " ", " ", " ", " ", " ", " ", " ", "*", "*", "*"],
    ["*", " ", "*", "*", "*", "*", " ", " ", " ", " ", " ", " ", "*"],
    ["*", " ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " ", "*"],
    ["*", "*", "*", "*", "x", "*", "*", "*", "*", "*", "*", "*", "*"]
]


def print_maze():
    for row in range(len(maze_lst)):
        for i in range(len(maze_lst[row])):
            print(maze_lst[row][i], end=" ")
        print()


start_position = [5, 0]
row = 5
column = 0
iter_count = 1
positions = []
move_back_pos = 0

positions.append((row, column))
while(maze_lst[row][column] != "x"):
    print("iteration: {}".format(iter_count))
    print("row: {}, column: {}".format(row, column))
    if(maze_lst[row][column + 1] == " "):
        if((row, column + 1) in positions):
            print("cannot move forward, position exist")
            print("move back postion: {}".format(move_back_pos))
            move_back_pos -= 1
            maze_lst[row][column] = "-"
            print(positions[move_back_pos])
            previous_position = list(positions[move_back_pos])
            row = previous_position[0]
            column = previous_position[1]
            maze_lst[row][column] = "o"
            print("Moved back")
        else:
            move_back_pos = 0
            column += 1
            positions.append((row, column))
            maze_lst[row][column] = "o"
            print("Moved forward")
    elif(maze_lst[row][column + 1] != " "):
        if(maze_lst[row][column + 1] == "x"):
            column += 1
            print("Found the way out of maze")
            continue
        print("cannot move forward")
        if(maze_lst[row - 1][column] == " "):
            if((row - 1, column) in positions):
                print("cannot move up, position exist")
                print("move back postion: {}".format(move_back_pos))
                move_back_pos -= 1
                maze_lst[row][column] = "-"
                print(positions[move_back_pos])
                previous_position = list(positions[move_back_pos])
                row = previous_position[0]
                column = previous_position[1]
                maze_lst[row][column] = "o"
                print("Moved back")
            else:
                move_back_pos = 0
                row -= 1
                positions.append((row, column))
                maze_lst[row][column] = "o"
                print("Moved Up")
        elif(maze_lst[row - 1][column] != " "):
            if(maze_lst[row - 1][column] == "x"):
                row -= 1
                print("Found the way out of maze")
                continue
            print("cannot move up")
            if(maze_lst[row + 1][column] == " "):
                if((row + 1, column) in positions):
                    print("cannot move down, position exist")
                    print("move back postion: {}".format(move_back_pos))
                    move_back_pos -= 1
                    maze_lst[row][column] = "-"
                    print(positions[move_back_pos])
                    previous_position = list(positions[move_back_pos])
                    row = previous_position[0]
                    column = previous_position[1]
                    maze_lst[row][column] = "o"
                    print("Moved back")
                else:
                    move_back_pos = 0
                    row += 1
                    positions.append((row, column))
                    maze_lst[row][column] = "o"
                    print("Moved down")
            elif(maze_lst[row + 1][column] != " "):
                if(maze_lst[row + 1][column] == "x"):
                    row += 1
                    print("Found the way out of maze")
                    continue
                print("cannot move down")
                if(maze_lst[row][column - 1] == " "):
                    if((row, column - 1) in positions):
                        print("cannot move west, position exist")
                        print("move back postion: {}".format(move_back_pos))
                        move_back_pos -= 1
                        maze_lst[row][column] = "-"
                        print(positions[move_back_pos])
                        previous_position = list(positions[move_back_pos])
                        row = previous_position[0]
                        column = previous_position[1]
                        maze_lst[row][column] = "o"
                        print("Moved back")
                    else:
                        move_back_pos = 0
                        column -= 1
                        positions.append((row, column))
                        maze_lst[row][column] = "o"
                        print("Moved down")

                elif(maze_lst[row][column - 1] != " "):
                    if(maze_lst[row][column - 1] == "x"):
                        column -= 1
                        print("Found the way out of maze")
                        continue
                    print("cannot move down")
                    move_back_pos -= 1
                    print("move back postion: {}".format(move_back_pos))
                    maze_lst[row][column] = "-"
                    previous_position = list(positions[move_back_pos])
                    row = previous_position[0]
                    column = previous_position[1]
                    maze_lst[row][column] = "o"
                    print("Moved back")
    iter_count += 1
print("found the exit after {} iterations".format(iter_count))
print("All positions from start to end including wrong path: {}".format(positions))
print(maze_str)
print_maze()
print("All 'o' is the right path to the finish, all '-' are wrong path taken and returned back")