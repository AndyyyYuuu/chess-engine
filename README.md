# Homemade Chess Engine: "StockYu"
An attempt at a chess engine, created for the HackChess hackathon. 
This project uses [python-chess](https://github.com/niklasf/python-chess) for move generation. 

### Algorithm Explanation, if it works as intended of course
In general, this algorithm works by recursively checking a tree of possible future positions and moves. The program assumes the worst case scenario, that is, the scenario in which the opponant makes the best moves. 
As a base case to prevent infinately searching down the tree of positions, the algorithm probes a certain depth before hitting a maximum, where it assigns the position a value based on a variety of factors such as number of pieces on both sides and whether or not a side has checkmated. A positive value means that white has the advantage, whereas a negative value is an advantage for black. These positional values are used by the search algorithm to find the worst case scenarios of each move and pick the move leading to the least undesirable positions. 
