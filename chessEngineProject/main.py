# StockYu Chess Engine
# Andy Yu
# StockYu in UCI Protocol

import chess
import stockyu
import sys
from time import time


board = None
time_left = 1800
time_update = None
IS_FAST = ("fast" in sys.argv)

def log_message(str):
    with open("log.txt", "a") as file:
        file.write(f"{str}\n")
def output(str):
    print(str)
    log_message(f"<< {str}")
    sys.stdout.flush()
log_message("\n-------- New Run --------")
while True:
    cmd = input().split()
    log_message("INPUT: " + " ".join(cmd))
    if cmd[0] == "uci":
        output("id name StockYu")
        output("id author Andy_Yu")
        output("uciok")
    elif cmd[0] == "isready":
        output("readyok")

    elif cmd[0] == "ucinewgame":
        board = chess.Board()
        log_message("new game")
    elif cmd[0] == "position":

        for i in range(1, len(cmd)):
            if cmd[i] == "moves":
                for j in cmd[i+1:]:
                    try:
                        board.push_uci(j)
                    except:
                        pass
            elif cmd[i] == "startpos":
                board.reset()

            else:
                try: board.set_fen(" ".join(cmd[i:]))
                except:pass
    elif cmd[0] == "go":
        # Make best move with time control
        for i in range(len(cmd[1:])):
            if (cmd[i+1] == "wtime" and board.turn == chess.WHITE) or (cmd[i+1] == "btime" and board.turn == chess.BLACK):
                try:
                    time_update = int(cmd[i+2])//1000
                except IndexError:
                    pass
        timestamp = time()
        if time_update is None:
            t = time_left
        else:
            t = time_update

        if t > 600 and not IS_FAST:
            output(f"bestmove {stockyu.evaluate(board, 3)}")
        elif t > 60:
            output(f"bestmove {stockyu.evaluate(board, 2)}")
        else:
            output(f"bestmove {stockyu.evaluate(board, 1)}")

        if time_update is None:
            time_left -= time() - timestamp
        else:
            time_update -= time() - timestamp

    elif cmd[0] == "quit":
        exit()
