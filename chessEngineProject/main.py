import chess, math, os
board = chess.Board()
piece_worths = {"K": 0, "k": 0, "Q": 9, "q": -9, "B": 3, "b": -3, "N": 3, "n": -3,"R": 4, "r": -4, "P": 1, "p": -1}
DEPTH = 2


def calc_advantage(board):
    piece_worth_value = 0
    for p in list(piece_worths.keys()):
        piece_worth_value += piece_worths.get(p)*str(board).count(p)
    if board.is_checkmate():
        if board.turn == chess.WHITE:
            return -math.inf
        else:
            return math.inf
    return piece_worth_value


def best_value(board, is_white, depth):
    if depth == 0:
        return calc_advantage(board)
    possible_moves = board.legal_moves
    best_move_values = []

    for a_move in possible_moves:
        board.push_san(str(a_move))
        best_move_values.append(best_value(board, not is_white, depth-1))
        if best_move_values[-1] is None:
            best_move_values.pop(-1)
        board.pop()
    if len(best_move_values) == 0:
        return None
    if is_white:
        return max(best_move_values)
    else:
        return min(best_move_values)


def evaluate(board):
    if board.turn == chess.BLACK:
        best_num = math.inf
    else:
        best_num = -math.inf
    best_move = None
    for a_move in board.legal_moves:
        board.push_san(str(a_move))
        value = best_value(board, True, DEPTH)
        if (board.turn == chess.BLACK and value > best_num) or (board.turn == chess.WHITE and value < best_num):
            best_move = a_move
            best_num = value
        board.pop()
    return best_move


best_value(board, True, DEPTH)
game_over_reasons = ("Checkmate", "Stalemate", "Insufficient material", "75-move rule", "Fivefold repetition", "50-move rule", "Threefold repetition")
while True:
    # input("Continue>>>")
    print("Calculating...")
    board.push_san(str(evaluate(board)))
    os.system("clear")
    print(("Black to move", "White to move")[board.turn])
    print(board)
    if board.is_game_over():
        print(game_over_reasons[board.outcome().termination.value-1])
        print(board.outcome().result())
        break


