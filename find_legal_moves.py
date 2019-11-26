# Assessment Solution

"""We are designing a 2D game and we have a game map that we represent by an integer matrix. For now, each cell can
be a wall (denoted by -1) or a blank space (0).

board = [
  [0,  0,  0, -1, -1],
  [0,  0, -1,  0,  0],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]

The player can move 1 space at a time up, down, left, or right. The player can't go through walls or land on a wall,
or go through the edges of the board.

Write a function that, given a board and a player starting position (represented as a row-column pair), returns all
of the possible next positions for the player.

Sample inputs (board, starting_position) and outputs (in any order):

findLegalMoves(board, (3, 1)) =>
  (3, 0), (4, 1)

findLegalMoves(board, (5, 3)) =>
  (5, 2), (5, 4), (4, 3), (6, 3)

findLegalMoves(board, (5, 1)) =>
  (6, 1), (4, 1), (5, 0), (5, 2)

findLegalMoves(board, (6, 0)) =>
  (5, 0), (6, 1)

findLegalMoves(board, (6, 4)) =>
  (5, 4), (6, 3)

findLegalMoves(board, (0, 0)) =>
  (0, 1), (1, 0)

findLegalMoves(board, (2, 2)) =>
  [empty]

"""


# my somewhat rudimentary solution
def find_legal_moves(board, position):
    """
    :param board: list[list][*]: our game board represented as an array or arrays
    :param position: position of the player on the board
    :return: tuple(possible moves)
    """
    global debug
    row = position[0]
    col = position[1]
    possible_moves = []
    len_board_rows = board.__len__()  # calculate for arbitrary board lengths
    len_board_cols = len(board[0])
    if debug:
        print('Rows:', len_board_rows)
        print('Columns', len_board_cols)
    up = -1
    down = -1
    left = -1
    right = -1
    if row != 0:  # if first row, cannot go up
        up = board[row - 1][col]
    if row != len_board_rows - 1:  # if last row, cannot go down
        down = board[row + 1][col]
    if col != 0:  # if first column, cannot got left
        left = board[row][col - 1]
    if col != len_board_cols - 1:  # if last column, cannot got left
        right = board[row][col + 1]
    # if element in array not 0 (-1 for wall)
    if up == 0:
        possible_moves.append((row - 1, col))
    if down == 0:
        possible_moves.append((row + 1, col))
    if left == 0:
        possible_moves.append((row, col - 1))
    if right == 0:
        possible_moves.append((row, col + 1))
    return possible_moves


if __name__ == '__main__':
    debug = False

    board = [
        [0, 0, 0, -1, -1],
        [0, 0, -1, 0, 0],
        [0, -1, 0, -1, 0],
        [0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    start1 = (3, 1)
    start2 = (5, 3)
    start3 = (5, 1)
    start4 = (6, 0)
    start5 = (6, 4)
    start6 = (0, 0)
    start7 = (2, 2)

    for i in [start1, start2, start3, start4, start5, start6, start7]:
        if debug:
            print('Running ' + str(i))
        print(find_legal_moves(board, i))
