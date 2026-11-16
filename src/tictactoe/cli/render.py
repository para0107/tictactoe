from src.tictactoe.cli import messages
from src.tictactoe.core.board import Board
from src.tictactoe.core.score import Score

_ROW_SEPARATOR = "---+---+---"
_ROW_LENGTH = 3


def render_board(board: Board) -> str:
    """Draw the grid, showing the cell number where no mark was placed."""
    cells = [str(mark) if mark else str(index + 1) for index, mark in enumerate(board)]
    rows = [
        " " + " | ".join(cells[start : start + _ROW_LENGTH])
        for start in range(0, len(cells), _ROW_LENGTH)
    ]
    return f"\n{_ROW_SEPARATOR}\n".join(rows)


def render_score(score: Score) -> str:
    """Format the session score line."""
    return messages.SCORE.format(x_wins=score.x_wins, o_wins=score.o_wins, draws=score.draws)
