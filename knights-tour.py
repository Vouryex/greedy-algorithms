import pandas as pd


def init_board(board_size, starting_point):
    board = []
    for i in range(0, board_size[0]):
        row = []
        for j in range(0, board_size[1]):
            if starting_point[0] == i and starting_point[1] == j:
                row.append('1')
            else:
                row.append('0')
        board.append(row)
    return board


def display_board(board):
    print(pd.DataFrame(board))


def valid_moves(board, knight_pos):
    moves_list = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
    next_moves = []
    for move in moves_list:
        next_row = knight_pos[0] + move[0]
        next_col = knight_pos[1] + move[1]

        if (next_row >= 0 and next_row < len(board)
                and next_col >= 0 and next_col < len(board[0])
                and board[next_row][next_col] == '0'):
            next_moves.append((next_row, next_col))
    return next_moves


def move(board, knight_pos, next_moves, move_count):
    moves_list = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
    min = (0, 0)
    min_value = float("inf")
    for next_move in next_moves:
        accessibility = 0
        for move in moves_list:
            accessible_row = next_move[0] + move[0]
            accessible_col = next_move[1] + move[1]
            if (accessible_row >= 0 and accessible_row < len(board)
                    and accessible_col >= 0 and accessible_col < len(board[0])
                    and board[accessible_row][accessible_col] == '0'):
                accessibility += 1
        if accessibility <= min_value:
            min = next_move
            min_value = accessibility
    board[min[0]][min[1]] = str(move_count+1)
    return (board, min, move_count+1)


def knights_tour(board_size, starting_point):
    board = init_board(board_size, starting_point)
    knight_pos = starting_point
    move_count = 1
    next_moves = valid_moves(board, knight_pos)

    while len(next_moves) != 0:
        board, knight_pos, move_count = move(board, knight_pos, next_moves, move_count)
        next_moves = valid_moves(board, knight_pos)

    display_board(board)


knights_tour((5, 4), (0, 0))
