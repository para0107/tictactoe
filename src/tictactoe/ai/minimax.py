from functools import cache

from src.tictactoe.core.board import Board
from src.tictactoe.core.mark import Mark
from src.tictactoe.core.rules import (
    get_next_mark,
    get_winner,
    is_draw,
    list_legal_moves,
    place_mark,
)


@cache
def _score_board(board: Board, mark: Mark) -> int:
    """Score for mark: win positive, draw zero, loss negative; faster wins score higher."""
    winner = get_winner(board)
    if winner is not None:
        empty_cells = board.count(None)
        return empty_cells + 1 if winner is mark else -(empty_cells + 1)
    if is_draw(board):
        return 0
    mover = get_next_mark(board)
    scores = [
        _score_board(place_mark(board, cell, mover), mark) for cell in list_legal_moves(board)
    ]
    return max(scores) if mover is mark else min(scores)


def choose_best_move(board: Board, mark: Mark) -> int:
    """Return the best cell for mark, the lowest index on a tie."""
    return max(
        list_legal_moves(board),
        key=lambda cell: _score_board(place_mark(board, cell, mark), mark),
    )
