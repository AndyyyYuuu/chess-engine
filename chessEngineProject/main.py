import chess, math, os, copy
chessboard = chess.Board()
piece_worths = {"K": 0, "k": 0, "Q": 9, "q": -9, "B": 3, "b": -3, "N": 3, "n": -3,"R": 4, "r": -4, "P": 1, "p": -1}
DEPTH = 2
possibilities = 0

def calc_advantage(board):
    global possibilities
    possibilities += 1
    piece_worth_value = 0
    for p in list(piece_worths.keys()):
        piece_worth_value += piece_worths.get(p)*str(board).count(p)
    if board.is_checkmate():
        if board.turn == chess.WHITE:
            return -math.inf
        else:
            return math.inf
    return piece_worth_value


    if depth == 0:
def best_value(input_board, is_white, depth):
    board = copy.copy(input_board)
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


best_value(chessboard, True, DEPTH)
game_over_reasons = ("Checkmate", "Stalemate", "Insufficient material", "75-move rule", "Fivefold repetition", "50-move rule", "Threefold repetition")
while True:
    print(f"Possibilities considered: {possibilities}")
    possibilities = 0
    print("Calculating...")
    chessboard.push_san(str(evaluate(chessboard)))
    os.system("clear")
    print(("Black to move", "White to move")[chessboard.turn])
    print(chessboard)
    if chessboard.is_game_over():
        print(game_over_reasons[chessboard.outcome().termination.value-1])
        print(chessboard.outcome().result())
        break



