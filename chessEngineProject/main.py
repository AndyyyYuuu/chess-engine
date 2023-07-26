# StockYu Chess Engine
# Andy Yu
# StockYu in UCI Protocol

import chess
import stockyu
from time import time


board = None
time_left = 1800
while True:
    cmd = input().split()
    if cmd[0] == "uci":
        print("id name StockYu")
        print("id author Andy Yu")
        print("uciok")
    elif cmd[0] == "isready":
        print("isreadyok")
    elif cmd[0] == "ucinewgame":
        board = chess.Board()
    elif cmd[0] == "position":
        if cmd[1] == "moves":
            for i in cmd[2:]:
                try:
                    board.push_uci(i)
                except:
                    pass
        elif cmd[1] == "startpos":
            board.reset_board()
    elif cmd[0] == "go":
        # Make best move with time control
        timestamp = time()
        if time_left > 600:
            print(f"bestmove {stockyu.evaluate(board, 3)}")
        elif time_left > 90:
            print(f"bestmove {stockyu.evaluate(board, 2)}")
        else:
            print(f"bestmove {stockyu.evaluate(board, 1)}")
        time_left -= time() - timestamp
    elif cmd[0] == "quit":
        exit()