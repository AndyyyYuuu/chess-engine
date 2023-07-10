import chess, math, random
board = chess.Board()
piece_worths = {"K": 0, "k": 0, "Q": 9, "q": -9, "B": 3, "b": -3, "N": 3, "n": -3,"R": 4, "r": -4, "P": 1, "p": -1}
DEPTH = 2
def calc_advantage(board):
    piece_worth_value = 0
    for p in list(piece_worths.keys()):
        piece_worth_value += piece_worths.get(p)*str(board).count(p)
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

print(board)
def best_move(board):
    max_num = -math.inf
    max_move = None
    for a_move in board.legal_moves:
        board.push_san(str(a_move))
        if best_value(board, True, DEPTH) > max_num:
            max_move = a_move
            max_num = best_value(board, True, DEPTH)
        board.pop()
    return max_move
while True:
    # input("Continue>>>")
    print("Chess Board: ")
    board.push_san(str(best_move(board)))
    print(board)

