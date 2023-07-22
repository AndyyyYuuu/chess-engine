# StockYu Engine Tester
# Andy Yu
# Runs a chess game of StockYu v. itself


import chess
import chess.pgn
import os
import stockyu

chessboard = chess.Board()
game = chess.pgn.Game()
moves = []

game_over_reasons = (
    "Checkmate",
    "Stalemate",
    "Insufficient material",
    "75-move rule",
    "Fivefold repetition",
    "50-move rule",
    "Threefold repetition"
)


while True:
    os.system("clear")
    print("STOCKYU EVALUATION BOARD")
    print(("Black to move", "White to move")[chessboard.turn])
    print(chessboard)
    print(", ".join(moves))
    if chessboard.is_game_over():
        print(game_over_reasons[chessboard.outcome().termination.value-1])
        print(chessboard.outcome().result())
        break
    print("Calculating...")
    move = stockyu.evaluate(chessboard, DEPTH=2)
    chessboard.push_san(str(move))
    moves.append(str(move))
