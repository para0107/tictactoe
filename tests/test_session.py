import random
from collections.abc import Callable
from itertools import cycle

from src.tictactoe.cli import messages
from src.tictactoe.cli.session import play_session
from src.tictactoe.core.mark import Mark
from tests.helpers import scripted


def run_session(read_line: Callable[[str], str]) -> list[str]:
    out: list[str] = []
    play_session(read_line, out.append, random.Random(0))
    return out


def test_two_player_x_win() -> None:
    out = run_session(scripted("1", "1", "4", "2", "5", "3", "n"))
    assert messages.WIN.format(mark=Mark.X) in out
    assert "Score - X: 1  O: 0  Draws: 0" in out
    assert out[-1] == messages.GOODBYE


def test_occupied_cell_reprompts() -> None:
    out = run_session(scripted("1", "1", "1", "4", "2", "5", "3", "n"))
    assert messages.CELL_OCCUPIED in out
    assert messages.WIN.format(mark=Mark.X) in out


def test_draw_then_rematch_accumulates_score() -> None:
    draw = ["1", "2", "3", "5", "4", "6", "8", "7", "9"]
    out = run_session(scripted("1", *draw, "y", *draw, "n"))
    assert out.count(messages.DRAW) == 2
    assert "Score - X: 0  O: 0  Draws: 2" in out


def test_hard_computer_game_ends() -> None:
    cells = cycle("123456789")

    def read_line(prompt: str) -> str:
        if prompt == messages.MODE_PROMPT:
            return "2"
        if prompt == messages.DIFFICULTY_PROMPT:
            return "hard"
        if prompt == messages.REMATCH_PROMPT:
            return "n"
        return next(cells)

    out = run_session(read_line)
    assert out[-1] == messages.GOODBYE
    assert messages.WIN.format(mark=Mark.X) not in out
