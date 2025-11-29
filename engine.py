import os
import time
import random
from pieces import WK, BK, E
from board import get_fresh_board, print_board
from pieces import PIECE2FUNC, PIECE2POINT


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


def choose_random_best_move(points_w_moves, color):
    points = [point_w_move[0] for point_w_move in points_w_moves]
    if color == "white":
        target_point = max(points)
    else:
        target_point = min(points)
    candidate_moves =  [point_w_move for point_w_move in points_w_moves if point_w_move[0] == target_point]
    return random.choice(candidate_moves)


def minimax(board, color, n):
    if n == 0:
        points_w_moves = []
        legal_moves = get_legal_moves(board, color)
        for move in legal_moves:
            prev_piece = make_move(board, move)
            move_point = evaluate_board(board)
            undo_move(board, move, prev_piece)
            points_w_moves.append((move_point, move))
        return points_w_moves
    else:
        points_w_moves = []
        legal_moves = get_legal_moves(board, color)
        for move in legal_moves:
            prev_piece = make_move(board, move)
            finished, winner = check_game_finished(board)

            if finished:
                if winner == color:
                    move_point = float('inf')
                else:
                    move_point = float('-inf')
                points_w_moves.append((move_point, move))
            else:
                if color == "white":
                    black_best_point_w_move = choose_random_best_move(minimax(board, "black", n - 1), "black")
                    points_w_moves.append((black_best_point_w_move[0], move))
                else:
                    white_best_point_w_move = choose_random_best_move(minimax(board, "white", n - 1), "white")
                    points_w_moves.append((white_best_point_w_move[0], move))
            undo_move(board, move, prev_piece)
        return points_w_moves


def minimax_player(board, color, n):
    points_w_moves = minimax(board, color, n)
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
    else:
        return sum(PIECE2POINT[piece] for piece in flat_board if piece < 0)


def evaluate_board(board):
    return get_color_score(board, "white") - get_color_score(board, "black")


def main():
    board = get_fresh_board()
    os.system("clear")
    print_board(board)
    color = "white"
    white_took, black_took = 0, 0
    for turn in range(2000):
        if color == "white":
            start = time.time()
            minimax_player(board, color, 2)
            white_took = time.time() - start
        else:
            start = time.time()
            minimax_player(board, color, 1)
            black_took = time.time() - start
        
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
            break

        color = "black" if color == "white" else "white"


if __name__ == "__main__":
    main()
