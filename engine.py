import os
import time
import random
from pieces import (WP, WN, WB, WR, WQ, WK,
                    BP, BN, BB, BR, BQ, BK, E)
from board import get_fresh_board, print_board
from pieces import PIECE2FUNC


def get_legal_moves(board, color):
    all_legal_moves = []
    for rank in range(8):
        for file in range(8):
            piece = board[rank][file]
            if piece == E:
                continue
            piece_color = 'white' if piece > 0 else 'black'
            if piece_color != color:
                continue
            if piece in PIECE2FUNC:
                legals = PIECE2FUNC[piece](board, color, (rank, file))
                for legal in legals:
                    all_legal_moves.append(((rank, file), legal, piece))

    return all_legal_moves


def make_move(board, move):
    current_place = move[0]
    target_place = move[1]
    piece = move[2]
    board[current_place[0]][current_place[1]] = 0
    board[target_place[0]][target_place[1]] = piece


def make_random_move(board, color):
    legal_moves = get_legal_moves(board, color)
    chosen_move = random.choice(legal_moves)
    make_move(board, chosen_move)


def main():
    os.system("clear")
    board = get_fresh_board()
    print_board(board)
    color = "white"
    for _ in range(20):
        time.sleep(0.5)
        os.system("clear")
        make_random_move(board, color)
        print_board(board)
        color = "black" if color == "white" else "white"


if __name__ == "__main__":
    main()
