# Play Against StockYu Engine
# Andy Yu
# Play against StockYu using SAN notation

import chess
import stockyu
import os

board = chess.Board()

while not board.is_game_over():
    os.system("clear")
    print("Your move!")
    print(board)
    while True:
        user = input(">>> ")
        try:
            board.push_san(user)
            break
        except:
            print("Error!")
    os.system("clear")
    print("Computer is thinking...")
    print(board)
    if board.is_game_over():
        break
    move = stockyu.evaluate(board, DEPTH=2)
    board.push_san(str(move))
print("Game over!")
