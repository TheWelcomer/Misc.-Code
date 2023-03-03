import re
def final_password():
    # read the board and directions from the files
    with open("board.txt") as f:
        board = [list(line.strip()) for line in f]
    with open("directions.txt") as f:
        directions = f.read().strip()

    # find the starting position and facing
    for j in range(len(board[0])):
        if board[0][j] == ".":
            x, y, facing = 0, j, 0
            break

    # split the directions into a list of instructions
    instructions = re.findall(r'\d+|\D',directions)

    for instruction in instructions:
        if instruction == "R":
            facing = (facing + 1) % 4
        elif instruction == "L":
            facing = (facing - 1) % 4
        else:
            distance = int(instruction)
            for i in range(distance):
                dx, dy = [0, 1, 0, -1][facing], [-1, 0, 1, 0][facing]
                if x + dx < 0:
                    x = len(board) - 1
                elif x + dx >= len(board):
                    x = 0
                elif y + dy < 0:
                    y = len(board[0]) - 1
                elif y + dy >= len(board[0]):
                    y = 0
                elif board[x + dx][y + dy] != "#":
                    x += dx
                    y += dy
                else:
                    facing = (facing + 2) % 4

    # calculate the final password
    password = 1000 * (x + 1) + 4 * (y + 1) + facing
    return password

print(final_password())