import chess, math, copy

piece_worths = {"K": 0, "k": 0, "Q": 9, "q": -9, "B": 3, "b": -3, "N": 3, "n": -3, "R": 4, "r": -4, "P": 1, "p": -1}
DEPTH = 2


def calc_advantage(board):
    if board.is_checkmate():
        if board.turn == chess.WHITE:
            return -math.inf
        else:
            return math.inf
    if board.can_claim_draw():
        return 0

    value = 0
    for p in list(piece_worths.keys()):
        value += piece_worths.get(p)*str(board).count(p)
    if board.turn == chess.WHITE:
        value += 0.1*board.legal_moves.count()
    else:
        value -= 0.1*board.legal_moves.count()

    return value


def best_value(input_board, move, is_white, depth):
    board = copy.copy(input_board)
    board.push_san(move)
    if depth == 0 or board.is_game_over():
        return calc_advantage(board)
    possible_moves = board.legal_moves
    best_move_values = []

    for a_move in possible_moves:
        best_move_values.append(best_value(board, str(a_move), not is_white, depth-1))
        #if best_move_values[-1] is None:
            #best_move_values.pop(-1)
    if len(best_move_values) == 0:
        return None
    if board.turn == chess.BLACK:
        return min(best_move_values)
    else:
        return max(best_move_values)


def evaluate(board):
    if board.turn == chess.BLACK:
        best_num = math.inf
    else:
        best_num = -math.inf
    best_move = None
    for a_move in board.legal_moves:

        value = best_value(board, str(a_move), True, DEPTH)
        if (board.turn == chess.BLACK and value < best_num) or (board.turn == chess.WHITE and value > best_num):
            best_move = a_move
            best_num = value
    return best_move