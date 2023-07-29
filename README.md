# Homemade Chess Engine: StockYu &nbsp;&nbsp;![icon_image](https://github.com/AndyyyYuuu/chess-engine/blob/main/icon.png?raw=true)
> *Every masterpiece has its cheap copy.*

&nbsp;&nbsp;&nbsp;&nbsp;An attempt at a chess engine, created for the HackChess hackathon. 

## How to Use
&nbsp;&nbsp;&nbsp;&nbsp;First install python-chess with the following command: 
```zsh
pip install chess
```
&nbsp;&nbsp;&nbsp;&nbsp;**To use the engine with UCI Protocol, run:**
```zsh
python3 <your path>/chessEngineProject/main.py
```
&nbsp;&nbsp;&nbsp;&nbsp;By default, the engine adjusts its depth based on time control. To always run at depth 2 for speedier responses, run: 
```zsh
python3 <your path>/chessEngineProject/main.py fast
```

### Useful Files
- `chessEngineProject/stockyu.py` Contains the engine's evaluation functions.
- `chessEngineProject/main.py` Runs StockYu with UCI protocol. 
- `chessEngineProject/demo.py` Runs and displays a game of StockYu vs. StockYu. 
- `chessEngineProject/play.py` Runs and displays a game of StockYu vs. the user using SAN notation. 

## Explanation
&nbsp;&nbsp;&nbsp;&nbsp;TL;DR: A simple minimax algorithm optimized with alpha-beta pruning that calculates up to 3 moves ahead. 

&nbsp;&nbsp;&nbsp;&nbsp;In general, this Minimax algorithm works by recursively checking a tree of possible future positions and moves. The program assumes the scenario in which both sides make the best moves and finds the move leading to the least disadvantaged positions. 

&nbsp;&nbsp;&nbsp;&nbsp;At the end of each branch of the Minimax tree, that is, whenever the probe hits max depth or detects the end of a game, the position is evaluated. The approximate value of a position, assuming no checkmates or draws, is calculated using this formula: 
```py
value = (white_piece_values - black_piece_values) + 0.1 * (white_mobility - black_mobility)
```
&nbsp;&nbsp;&nbsp;&nbsp;This value is used in the Minimax algorithm to determine the best moves; to white, this means maximizing the value of a position, while black seeks to minimize it. 


### Thanks to: 
- [HackChess 2023](https://hackchess.devpost.com/) for providing an opportunity for this chess engine to face some very formidable opponents. 
- [python-chess](https://github.com/niklasf/python-chess) for its move generation and checkmate/draw detection functions. 
