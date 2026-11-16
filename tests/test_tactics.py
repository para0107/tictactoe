import random

import pytest

from src.tictactoe.ai.computer import choose_move
from src.tictactoe.ai.difficulty import Difficulty
from src.tictactoe.ai.tactics import choose_random_move, choose_tactical_move
from src.tictactoe.core.board import EMPTY_BOARD, Board
from src.tictactoe.core.mark import Mark
from src.tictactoe.core.rules import list_legal_moves

X = Mark.X
O = Mark.O
BOARDS: list[Board] = [
    EMPTY_BOARD,
    (X, None, None, None, O, None, None, None, None),
    (X, O, X, None, O, None, None, None, None),
]


def test_random_move_is_always_legal() -> None:
    rng = random.Random(1)
    for board in BOARDS:
        for _ in range(50):
            assert choose_random_move(board, rng) in list_legal_moves(board)


def test_medium_takes_own_win_over_block() -> None:
    board: Board = (X, X, None, O, O, None, None, None, None)
    assert choose_tactical_move(board, X, random.Random(0)) == 2
    assert choose_tactical_move(board, O, random.Random(0)) == 5


def test_medium_blocks_when_no_own_win() -> None:
    board: Board = (X, X, None, None, O, None, None, None, None)
    assert choose_tactical_move(board, O, random.Random(0)) == 2


@pytest.mark.parametrize("difficulty", [Difficulty.EASY, Difficulty.MEDIUM])
def test_choose_move_returns_legal_move(difficulty: Difficulty) -> None:
    rng = random.Random(2)
    for board in BOARDS:
        assert choose_move(board, O, difficulty, rng) in list_legal_moves(board)
