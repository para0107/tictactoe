# tictactoe

Terminal tic-tac-toe: two players, or one against the computer (easy, medium, hard).

## Commands

Run from the repo root.

- Install: `uv sync`
- Run: `uv run python -m src.tictactoe`
- Lint: `uv run ruff check .`
- Format: `uv run ruff format .`
- Test: `uv run pytest`

## Where the code lives

- `src/tictactoe/core/`: mark, board, rules, score
- `src/tictactoe/ai/`: difficulty, tactics, minimax, computer
- `src/tictactoe/cli/`: messages, render, prompts, session
- `src/tictactoe/__main__.py`: `main()`
- `tests/`: one test file per logic module

## Conventions

- `core/` and `ai/` stay free of I/O.
- `cli/` holds no game rules.
- User-facing strings live in `cli/messages.py`.
- Imports use the `src.tictactoe` root; there is no `src/__init__.py`.
- No comments in code; docstrings are one line.

## Notes kept by cw
- Run checks with `uv run ruff check .` and `uv run pytest` from the repo root; imports are rooted at `src.tictactoe` and there is no src/__init__.py.
