# board = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("--------------------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def get_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)

    return None

# check if input to the puzzle is valid
# check if each column has the same number
# check if each row has the same nubmer
# check if each section has the same number


def check(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    sec_x = pos[1] // 3
    sec_y = pos[0] // 3

    for i in range(sec_y * 3, sec_y * 3 + 3):
        for j in range(sec_x*3, sec_x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


# solve this puzzle with backtrack algorithm (RECURSIVE)
# going from the top row to bottom row and from the left column to the right column
# check if the input is correct,
#       if it is, move on to the next empty space
#       else, reset value to 0 to the last input

def solve(board):
    # no more empty space, puzzle solved
    empty = get_empty(board)
    if not empty:
        return True
    else:
        row, col = empty

        for i in range(1, 10):
            if check(board, i, (row, col)):
                board[row][col] = i

                if solve(board):
                    return True

                # reset the value
                board[row][col] = 0

        return False


# print_board(board)
# solve(board)
# print("##############################")
# print_board(board)
