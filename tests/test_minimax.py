import random

import pytest

from src.tictactoe.ai.computer import choose_move
from src.tictactoe.ai.difficulty import Difficulty
from src.tictactoe.core.board import EMPTY_BOARD, Board
from src.tictactoe.core.mark import Mark
from src.tictactoe.core.rules import (
    get_next_mark,
    get_winner,
    is_draw,
    list_legal_moves,
    place_mark,
)


def _assert_ai_never_loses(board: Board, ai_mark: Mark, rng: random.Random) -> None:
    if get_winner(board) is not None or is_draw(board):
        assert get_winner(board) is not ai_mark.opponent
        return
    if get_next_mark(board) is ai_mark:
        cell = choose_move(board, ai_mark, Difficulty.HARD, rng)
        _assert_ai_never_loses(place_mark(board, cell, ai_mark), ai_mark, rng)
        return
    for cell in list_legal_moves(board):
        _assert_ai_never_loses(place_mark(board, cell, ai_mark.opponent), ai_mark, rng)


@pytest.mark.parametrize("ai_mark", [Mark.X, Mark.O])
def test_hard_ai_never_loses(ai_mark: Mark) -> None:
    _assert_ai_never_loses(EMPTY_BOARD, ai_mark, random.Random(0))
