from pieces import (WP, WN, WB, WR, WQ, WK,
                    BP, BN, BB, BR, BQ, BK, E)


def get_fresh_board():
    board = [
        [WR, WN, WB, WQ, WK, WB, WN, WR],
        [WP, WP, WP, WP, WP, WP, WP, WP],
        [E,  E,  E,  E,  E,  E,  E,  E],
        [E,  E,  E,  E,  E,  E,  E,  E],
        [E,  E,  E,  E,  E,  E,  E,  E],
        [E,  E,  E,  E,  E,  E,  E,  E],
        [BP, BP, BP, BP, BP, BP, BP, BP],
        [BR, BN, BB, BQ, BK, BB, BN, BR]
    ]
    return board


def print_board(board):
    for row in board:
        row_str = ""
        for piece in row:
            if piece >= 0:
                row_str += " " + str(piece)
            else:
                row_str += str(piece)
        print(row_str)

