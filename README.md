# Homemade Chess Engine: "StockYu"
> *Every masterpiece has its cheap copy.*

&nbsp;&nbsp;&nbsp;&nbsp;An attempt at a chess engine, created for the HackChess hackathon. 

### Explanation
&nbsp;&nbsp;&nbsp;&nbsp;TL;DR: A simple minimax algorithm optimized with alpha-beta pruning that calculates 3 moves ahead. 

&nbsp;&nbsp;&nbsp;&nbsp;In general, this Minimax algorithm works by recursively checking a tree of possible future positions and moves. The program assumes the scenario in which both sides make the best moves and finds the move leading to the least disadvantaged positions. 

&nbsp;&nbsp;&nbsp;&nbsp;At the end of each branch of the Minimax tree, that is, whenever the probe hits max depth or detects the end of a game, the position is evaluated. The value of the position is calculated using this formula: 
```py
value = (white_piece_values - black_piece_values) + mobility * 0.1
```
&nbsp;&nbsp;&nbsp;&nbsp;This value is used in the Minimax algorithm to determine the best moves; to white, this means maximizing the value of a position, while black seeks to minimize it. 

### Files
- `stockyu.py` Contains the engine's evaluation functions.
- `main.py` Runs a game of StockYu vs. user input using UCI notation.
- `demo.py` Runs and displays a game of StockYu vs. itself. 

### Thanks to: 
- [HackChess 2023](https://hackchess.devpost.com/) for providing an opportunity for this chess engine to face some very formidable opponents. 
- [python-chess](https://github.com/niklasf/python-chess) for its move generation and checkmate/draw detection functions. 
