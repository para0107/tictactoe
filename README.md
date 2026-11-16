# tictactoe

A terminal tic-tac-toe game in Python. Modes: two players on one keyboard, or one player against the computer. The computer has three difficulty levels: easy plays random legal moves, medium blocks your wins and takes its own, hard uses minimax and never loses. The board shows numbered cells 1-9 and the player types a number. Detect a win or a draw, then offer a rematch; keep the score for the session. Keep the game logic (board, rules, winner, AI) separate from the terminal input and output, so it is fully unit tested: every win line, the draw, illegal moves, and that the hard AI never loses against every possible sequence of moves.

## Requirements

- Python 3.13
- [uv](https://docs.astral.sh/uv/)

## Install

```bash
uv sync
```

## Run

```bash
uv run python -m src.tictactoe
```

## Lint

```bash
uv run ruff check .
uv run ruff format .
```

## Test

```bash
uv run pytest
```

## Layout

- `src/tictactoe/core/`: pure game logic, no I/O
  - `mark.py`: the `Mark` enum (X and O)
  - `board.py`: the `Board` type, board size and the win lines
  - `rules.py`: placing marks, winner, draw, next mark, legal moves, illegal-move error
  - `score.py`: the session score
- `src/tictactoe/ai/`: the computer player, no I/O
  - `difficulty.py`: the `Difficulty` enum
  - `tactics.py`: easy random move, medium win and block
  - `minimax.py`: cached minimax for hard
  - `computer.py`: `choose_move`, which picks the strategy by difficulty
- `src/tictactoe/cli/`: terminal input and output only
  - `messages.py`: every user-facing string
  - `render.py`: board and score rendering
  - `prompts.py`: validated readers for mode, difficulty, cell and rematch
  - `session.py`: the game loop and the session with rematches
- `src/tictactoe/__main__.py`: entry point, `main()`
- `tests/`: unit tests, one file per logic module, plus the exhaustive hard-AI check
