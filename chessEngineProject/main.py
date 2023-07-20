# StockYu Chess Engine
# Andy Yu
# StockYu in UCI Protocol

import chess
import stockyu
board = None
while True:
    cmd = input().split()
    try:
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
                board.push_uci(cmd[2])
            elif cmd[1] == "startpos":
                board.reset_board()
        elif cmd[0] == "go":
            print(f"bestmove {stockyu.evaluate(board)}")
        elif cmd[0] == "quit":
            exit()
    except:
        pass