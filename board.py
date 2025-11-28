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


PIECE_SYMBOLS = {
    WK: '♔', WQ: '♕', WR: '♖', WB: '♗', WN: '♘', WP: '♙',
    BK: '♚', BQ: '♛', BR: '♜', BB: '♝', BN: '♞', BP: '♟',
    E: '·'
}


def print_board(board):
    print("  a b c d e f g h")
    print("  ---------------")
    for rank in range(7, -1, -1):
        row_str = f"{rank + 1}|"
        for file in range(8):
            piece = board[rank][file]
            symbol = PIECE_SYMBOLS.get(piece, '?')
            row_str += f"{symbol} "
        print(row_str)
    print("  ---------------")
    print("  a b c d e f g h")

