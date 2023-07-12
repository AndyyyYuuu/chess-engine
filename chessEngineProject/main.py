import chess
import os
import stockyu

chessboard = chess.Board()

game_over_reasons = (
    "Checkmate",
    "Stalemate",
    "Insufficient material",
    "75-move rule",
    "Fivefold repetition",
    "50-move rule",
    "Threefold repetition"
)

print("Loading...")
while True:
    os.system("clear")
    print("STOCKYU EVALUATION BOARD")
    print(("Black to move", "White to move")[chessboard.turn])
    print(chessboard)
    if chessboard.is_game_over():
        print(game_over_reasons[chessboard.outcome().termination.value-1])
        print(chessboard.outcome().result())
        break
    possibilities = 0
    print("Calculating...")
    chessboard.push_san(str(stockyu.evaluate(chessboard)))
