board_test = [
    [4, 8, 9, 0, 0, 2, 0, 1, 0],
    [0, 5, 0, 8, 0, 1, 0, 9, 4],
    [3, 0, 6, 0, 4, 9, 8, 7, 0],

    [2, 0, 8, 0, 0, 0, 4, 6, 0],
    [5, 4, 7, 3, 0, 6, 0, 0, 1],
    [0, 9, 0, 0, 8, 0, 7, 0, 0],

    [8, 0, 3, 0, 1, 0, 9, 0, 0],
    [9, 0, 4, 0, 6, 0, 1, 5, 0],
    [0, 6, 0, 0, 2, 0, 0, 0, 7]
]


def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None, None


def is_valid(board, number, row, col):
    row_fields = board[row]
    if number in row_fields:
        return False

    col_fields = [board[r][col] for r in range(9)]
    if number in col_fields:
        return False

    row_field = (row // 3) * 3
    col_field = (col // 3) * 3
    for r in range(row_field, row_field + 3):
        for c in range(col_field, col_field + 3):
            if board[r][c] == number:
                return False

    return True


def solve_sudoku(board):
    row, col = find_empty(board)
    if row is None:
        return True

    for number in range(1, 10):
        if is_valid(board, number, row, col):
            board[row][col] = number
            if solve_sudoku(board):
                return True

        board[row][col] = 0

    return False


def print_board(board):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print('- - - - - - - - - - - - ')
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")
            if c == 8:
                print(board[r][c])
            else:
                print(str(board[r][c]) + ' ', end="")


print_board(board_test)
print("")
print(solve_sudoku(board_test))
print("")
print_board(board_test)
