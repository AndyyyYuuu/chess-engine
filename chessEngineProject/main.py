import chess, math
board = chess.Board()

def calc_advantage(board):
    return 1
def best_move(board, is_white, depth):
    if depth == 0:
        return calc_advantage
    possible_moves = board.legal_moves
    best_move_values = []

    for a_move in possible_moves:
        board.push_san(str(a_move))
        best_move_values.append(best_move(board, not is_white, depth-1))
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
max_num = -math.inf
max_move = None
for a_move in board.legal_moves:
    board.push_san(str(a_move))
    if (best_move(board, True, 3) > max_num):
        max_move = a_move
    board.pop()
print(str(max_move))
