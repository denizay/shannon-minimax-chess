E = 0	# Empty

WP = 1	# White Pawn
WN = 2	# White Knight
WB = 3	# White Bishop
WR = 4	# White Rook
WQ = 5	# White Queen
WK = 6	# White King

BP = -1	# Black Pawn
BN = -2	# Black Knight
BB = -3	# Black Bishop
BR = -4	# Black Rook
BQ = -5	# Black Queen
BK = -6	# Black King

def get_pawn_legals(board, color, position):
    legal_moves = []
    rank, file = position
    if color == 'white':
        if rank == 7:
            return []
        if board[rank+1][file] == 0:
            legal_moves.append((rank+1, file))
        if rank == 1 and board[rank+1][file] == 0 and board[rank+2][file] == 0:
            legal_moves.append((rank+2, file))
        if file > 0 and board[rank+1][file-1] < 0:
            legal_moves.append((rank+1, file-1))
        if file < 7 and board[rank+1][file+1] < 0:
            legal_moves.append((rank+1, file+1))
    else:
        if rank == 0:
            return []
        if board[rank-1][file] == 0:
            legal_moves.append((rank-1, file))
        if rank == 6 and board[rank-1][file] == 0 and board[rank-2][file] == 0:
            legal_moves.append((rank-2, file))
        if file > 0 and board[rank-1][file-1] > 0:
            legal_moves.append((rank-1, file-1))
        if file < 7 and board[rank-1][file+1] > 0:
            legal_moves.append((rank-1, file+1))
    return legal_moves


def is_on_board(position):
    rank, file = position
    return 0 <= rank < 8 and 0 <= file < 8


def get_knight_legals(board, color, position):
    legal_moves = []
    rank, file = position
    moves = [
        (rank-2, file-1), (rank-2, file+1),
        (rank-1, file-2), (rank-1, file+2),
        (rank+1, file-2), (rank+1, file+2),
        (rank+2, file-1), (rank+2, file+1)
    ]
    for r, f in moves:
        if is_on_board((r, f)):
            piece = board[r][f]
            if piece == 0:
                legal_moves.append((r, f))
            else:
                piece_color = 'white' if piece > 0 else 'black'
                if piece_color != color:
                    legal_moves.append((r, f))
    return legal_moves


def get_sliding_legals(board, color, position, directions):
    legal_moves = []
    rank, file = position
    for dr, df in directions:
        r, f = rank + dr, file + df
        while is_on_board((r, f)):
            piece = board[r][f]
            if piece == 0:
                legal_moves.append((r, f))
            else:
                piece_color = 'white' if piece > 0 else 'black'
                if piece_color != color:
                    legal_moves.append((r, f))
                break
            r += dr
            f += df
    return legal_moves


def get_bishop_legals(board, color, position):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    return get_sliding_legals(board, color, position, directions)


def get_rook_legals(board, color, position):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return get_sliding_legals(board, color, position, directions)


def get_queen_legals(board, color, position):
    directions = [
        (-1, -1), (-1, 1), (1, -1), (1, 1),
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]
    return get_sliding_legals(board, color, position, directions)


def get_king_legals(board, color, position):
    legal_moves = []
    rank, file = position
    moves = [
        (rank-1, file-1), (rank-1, file), (rank-1, file+1),
        (rank, file-1),                 (rank, file+1),
        (rank+1, file-1), (rank+1, file), (rank+1, file+1)
    ]
    for r, f in moves:
        if is_on_board((r, f)):
            piece = board[r][f]
            if piece == 0:
                legal_moves.append((r, f))
            else:
                piece_color = 'white' if piece > 0 else 'black'
                if piece_color != color:
                    legal_moves.append((r, f))
    return legal_moves


PIECE2FUNC = {
        WP: get_pawn_legals,
        BP: get_pawn_legals,
        WN: get_knight_legals,
        BN: get_knight_legals,
        WB: get_bishop_legals,
        BB: get_bishop_legals,
        WR: get_rook_legals,
        BR: get_rook_legals,
        WQ: get_queen_legals,
        BQ: get_queen_legals,
        WK: get_king_legals,
        BK: get_king_legals,
        }
