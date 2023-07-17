# StockYu Chess Engine
# Andy Yu
# Use evaluate(chess.Board) to get best move

import chess, math, copy

piece_worths = {"K": 0, "k": 0, "Q": 9, "q": -9, "B": 3, "b": -3, "N": 3, "n": -3, "R": 5, "r": -5, "P": 1, "p": -1}
DEPTH = 2
function_runs = 0


# Returns the value of a position
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


# Returns the value of the worst-case scenario
def best_value(input_board, move, depth, alpha, beta):
    global function_runs
    function_runs += 1

    board = copy.copy(input_board)
    board.push_san(move)

    # End node: max depth reached or game over case
    if depth == 0 or board.is_game_over():
        return calc_advantage(board)

    # Find the value of the move assuming both sides play most optimally
    best_move_value = (math.inf, -math.inf)[board.turn]
    for a_move in board.legal_moves:
        v = best_value(board, str(a_move), depth-1, alpha, beta)
        if (board.turn == chess.WHITE and v > best_move_value) or (board.turn == chess.BLACK and v < best_move_value):
            best_move_value = v
        if board.turn == chess.WHITE:
            alpha = max(alpha, v)
        else:
            beta = min(beta, v)
        if beta <= alpha:
            break
    return best_move_value


# Returns the best move on the given board
def evaluate(board):
    global function_runs
    function_runs = 0

    # Find move yielding the best value from best_value()
    if board.turn == chess.BLACK:
        best_num = math.inf
    else:
        best_num = -math.inf
    best_move = None

    for a_move in board.legal_moves:
        value = best_value(board, str(a_move), DEPTH, -math.inf, math.inf)
        if (board.turn == chess.BLACK and value < best_num) or (board.turn == chess.WHITE and value > best_num):
            best_move = a_move
            best_num = value
    print(f"Evaluated positions: {function_runs}")
    return best_move