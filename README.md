# Shannon's Minimax Chess Engine

A lightweight Python chess engine inspired by Claude Shannon's 1950 paper, "Programming a Computer for Playing Chess"

This project implements a Type A strategy (as defined by Shannon), utilizing a full-width Minimax search algorithm with a material-based evaluation function.

## How to Run

No external dependencies are required. Just run the engine with Python 3:

```bash
python engine.py
```

### Simplified Rules

To focus on the algorithmic implementation, the game ends when a King is physically removed from the board.
