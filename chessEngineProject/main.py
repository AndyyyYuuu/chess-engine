# StockYu Chess Engine
# Andy Yu
# StockYu in UCI Protocol

import chess
import stockyu
from time import time


board = None
time_left = 1800
time_update = None
while True:
    cmd = input().split()
    if cmd[0] == "uci":
        print("id name StockYu")
        print("id author Andy_Yu")
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
        else:
            try: board.set_fen(cmd[1])
            except:pass
    elif cmd[0] == "go":
        # Make best move with time control
        print(cmd)
        for i in range(len(cmd[1:])):
            if (cmd[i+1] == "wtime" and board.turn == chess.WHITE) or (cmd[i+1] == "btime" and board.turn == chess.BLACK):
                try:
                    time_update = int(cmd[i+2])//1000
                except IndexError:
                    pass
        timestamp = time()
        try:
            if time_update is None:

                if time_left > 600:
                    print(f"bestmove {stockyu.evaluate(board, 3)}")
                elif time_left > 90:
                    print(f"bestmove {stockyu.evaluate(board, 2)}")
                else:
                    print(f"bestmove {stockyu.evaluate(board, 1)}")
                time_left -= time() - timestamp
            else:
                if time_update > 600:
                    print(f"bestmove {stockyu.evaluate(board, 3)}")
                elif time_update > 90:
                    print(f"bestmove {stockyu.evaluate(board, 2)}")
                else:
                    print(f"bestmove {stockyu.evaluate(board, 1)}")
                time_update -= time() - timestamp
        except:pass
    elif cmd[0] == "quit":
        exit()