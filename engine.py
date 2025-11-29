import os
import random
import time

from board import get_fresh_board, print_board
from pieces import BK, WK, E, PIECE2FUNC, PIECE2POINT


def get_legal_moves(board, color):
    all_legal_moves = []
    for rank in range(8):
        for file in range(8):
            piece = board[rank][file]
            if piece == E:
                continue
            piece_color = "white" if piece > 0 else "black"
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
    target_piece = board[target_place[0]][target_place[1]]
    board[target_place[0]][target_place[1]] = piece
    return target_piece


def undo_move(board, move, prev_piece):
    current_place = move[0]
    target_place = move[1]
    piece = move[2]
    board[current_place[0]][current_place[1]] = piece
    board[target_place[0]][target_place[1]] = prev_piece


def make_random_move(board, color):
    legal_moves = get_legal_moves(board, color)
    chosen_move = random.choice(legal_moves)
    make_move(board, chosen_move)


def get_opponent(color):
    return "black" if color == "white" else "white"


def is_maximizing(color):
    return color == "white"


def choose_random_best_move(points_w_moves, color):
    points = [point_w_move[0] for point_w_move in points_w_moves]
    target_point = max(points) if is_maximizing(color) else min(points)
    candidate_moves = [
        point_w_move
        for point_w_move in points_w_moves
        if point_w_move[0] == target_point
    ]
    return random.choice(candidate_moves)


def minimax(board, color, depth):
    if depth == 0 or check_game_finished(board)[0]:
        return evaluate_board(board)
    best_point = float("-inf") if is_maximizing(color) else float("inf")
    legal_moves = get_legal_moves(board, color)
    for move in legal_moves:
        prev_piece = make_move(board, move)
        selector = max if is_maximizing(color) else min
        best_point = selector(
            best_point, minimax(board, get_opponent(color), depth - 1)
        )
        undo_move(board, move, prev_piece)
    return best_point


def minimax_player(board, color, depth):
    legal_moves = get_legal_moves(board, color)
    points_w_moves = []
    for move in legal_moves:
        prev_piece = make_move(board, move)
        point = minimax(board, get_opponent(color), depth - 1)
        points_w_moves.append((point, move))
        undo_move(board, move, prev_piece)
    best_point_w_move = choose_random_best_move(points_w_moves, color)
    make_move(board, best_point_w_move[1])


def check_game_finished(board):
    flat_board = [piece for row in board for piece in row]
    if WK not in flat_board:
        return True, "black"
    if BK not in flat_board:
        return True, "white"
    return False, None


def get_color_score(board, color):
    flat_board = [piece for row in board for piece in row]
    if color == "white":
        return sum(PIECE2POINT[piece] for piece in flat_board if piece > 0)
    return sum(PIECE2POINT[piece] for piece in flat_board if piece < 0)


def evaluate_board(board):
    return get_color_score(board, "white") - get_color_score(board, "black")


def main():
    board = get_fresh_board()
    os.system("clear")
    print_board(board)
    color = "white"
    white_took, black_took = 0, 0
    white_all_times, black_all_times = [], []
    for turn in range(2000):
        if color == "white":
            start = time.time()
            minimax_player(board, color, 3)
            white_took = time.time() - start
            white_all_times.append(white_took)
        else:
            start = time.time()
            minimax_player(board, color, 2)
            black_took = time.time() - start
            black_all_times.append(black_took)

        os.system("clear")
        print_board(board)

        white_score = get_color_score(board, "white")
        black_score = get_color_score(board, "black")
        points_diff = white_score - black_score
        print(f"White score: {white_score} Black score: {black_score}")
        print(f"Points diff: {points_diff}")
        print(f"Turn: {turn}")
        print(f"White took: {white_took:.2f} seconds")
        print(f"Black took: {black_took:.2f} seconds")

        finished, winner = check_game_finished(board)

        if finished:
            print(f"Game finished. {winner} wins!")
            print(
                f"White avg time per move: {sum(white_all_times)/len(white_all_times)}"
            )
            print(
                f"Black avg time per move: {sum(black_all_times)/len(black_all_times)}"
            )
            break

        color = get_opponent(color)


if __name__ == "__main__":
    main()
