from src.tictactoe.ai.difficulty import Difficulty
from src.tictactoe.cli.prompts import (
    Mode,
    read_cell,
    read_difficulty,
    read_mode,
    read_rematch,
)
from src.tictactoe.core.mark import Mark
from tests.helpers import scripted


def test_read_mode_valid_and_retry() -> None:
    out: list[str] = []
    assert read_mode(scripted("2"), out.append) is Mode.VS_COMPUTER
    assert read_mode(scripted("abc", "1"), out.append) is Mode.TWO_PLAYERS


def test_read_mode_reports_invalid_input() -> None:
    out: list[str] = []
    read_mode(scripted("abc", "1"), out.append)
    assert len(out) == 2


def test_read_difficulty_word_and_number() -> None:
    out: list[str] = []
    assert read_difficulty(scripted("Hard"), out.append) is Difficulty.HARD
    assert read_difficulty(scripted("2"), out.append) is Difficulty.MEDIUM
    assert read_difficulty(scripted("abc", "0", "easy"), out.append) is Difficulty.EASY


def test_read_cell_returns_index() -> None:
    assert read_cell(scripted("1"), [].append, Mark.X) == 0
    assert read_cell(scripted("9"), [].append, Mark.O) == 8


def test_read_cell_reprompts_on_bad_input() -> None:
    out: list[str] = []
    assert read_cell(scripted("abc", "0", "10", "5"), out.append, Mark.X) == 4
    assert len(out) == 3


def test_read_rematch() -> None:
    assert read_rematch(scripted("y"))
    assert read_rematch(scripted("YES"))
    assert not read_rematch(scripted("n"))
    assert not read_rematch(scripted("maybe"))
