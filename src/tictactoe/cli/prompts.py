from collections.abc import Callable
from enum import StrEnum

from src.tictactoe.ai.difficulty import Difficulty
from src.tictactoe.cli import messages
from src.tictactoe.core.board import BOARD_SIZE
from src.tictactoe.core.mark import Mark

ReadLine = Callable[[str], str]
WriteLine = Callable[[str], None]

_DIFFICULTY_CHOICES = {
    "1": Difficulty.EASY,
    "2": Difficulty.MEDIUM,
    "3": Difficulty.HARD,
}
_REMATCH_ANSWERS = frozenset({"y", "yes"})


class Mode(StrEnum):
    """Who plays against whom."""

    TWO_PLAYERS = "1"
    VS_COMPUTER = "2"


def read_mode(read_line: ReadLine, write_line: WriteLine) -> Mode:
    """Ask until the answer is a valid mode."""
    write_line(messages.MODE_MENU)
    while True:
        answer = read_line(messages.MODE_PROMPT).strip()
        try:
            return Mode(answer)
        except ValueError:
            write_line(messages.INVALID_INPUT)


def read_difficulty(read_line: ReadLine, write_line: WriteLine) -> Difficulty:
    """Ask until the answer is a difficulty word or its number."""
    write_line(messages.DIFFICULTY_MENU)
    while True:
        answer = read_line(messages.DIFFICULTY_PROMPT).strip().lower()
        if answer in _DIFFICULTY_CHOICES:
            return _DIFFICULTY_CHOICES[answer]
        try:
            return Difficulty(answer)
        except ValueError:
            write_line(messages.INVALID_INPUT)


def read_cell(read_line: ReadLine, write_line: WriteLine, mark: Mark) -> int:
    """Ask until the answer is a number 1-9 and return it as an index 0-8."""
    while True:
        answer = read_line(messages.MOVE_PROMPT.format(mark=mark)).strip()
        if not answer.isdecimal():
            write_line(messages.INVALID_INPUT)
        elif not 1 <= int(answer) <= BOARD_SIZE:
            write_line(messages.CELL_OUT_OF_RANGE)
        else:
            return int(answer) - 1


def read_rematch(read_line: ReadLine) -> bool:
    """Return True only for y or yes."""
    return read_line(messages.REMATCH_PROMPT).strip().lower() in _REMATCH_ANSWERS
