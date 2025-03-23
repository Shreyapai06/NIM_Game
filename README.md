# Red-Blue Nim Game

This is a Python implementation of the Red-Blue Nim game, where two players (human vs. computer) take turns removing marbles from two piles (red and blue). The game can be played in either **standard** or **misere** mode, and the computer uses the **Minimax algorithm with Alpha-Beta Pruning** for optimal decision-making.

## How to Play
1. The game starts by asking the user to enter the number of red and blue marbles.
2. The user selects the game mode:
   - **Standard Mode**: The player who takes the last move loses.
   - **Misere Mode**: The player who takes the last move wins.
3. The user chooses whether they or the computer will go first.
4. Players take turns removing 1 or 2 marbles from either the red or blue pile.
5. The game ends when one pile is empty, and the winner is determined based on the selected mode.

## Features
- **Minimax Algorithm with Alpha-Beta Pruning** for efficient move selection.
- **User Input Handling** with error checking.
- **Flexible Move Order**: The computer picks the best move dynamically.
- **Interactive Gameplay** with clear instructions.

## Installation & Execution
### Prerequisites
- Python 3.x

### Running the Game
```sh
python nim_game_ai.py
```
Follow the prompts to enter the initial conditions and play against the AI.

## Example Gameplay
```
Enter number of red marbles: 3
Enter number of blue marbles: 4
Enter game version (standard/misere): standard
Who plays first? (human/computer): human

Current state: 3 red, 4 blue
Your move (format: red/blue 1/2): blue 2

Computer's turn:
Computer removes 1 red marble(s)
...
Game over. Human loses.
Computer wins!
```
