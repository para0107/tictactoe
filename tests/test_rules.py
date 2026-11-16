import pytest

from src.tictactoe.core.board import BOARD_SIZE, EMPTY_BOARD, WIN_LINES, Board
from src.tictactoe.core.mark import Mark
from src.tictactoe.core.rules import (
    IllegalMoveError,
    get_next_mark,
    get_winner,
    is_draw,
    list_legal_moves,
    place_mark,
)

X, O = Mark.X, Mark.O
DRAWN_BOARD: Board = (X, O, X, X, O, O, O, X, X)
X_WON_BOARD: Board = (X, X, X, O, O, None, None, None, None)


def board_with_line(line: tuple[int, int, int], mark: Mark) -> Board:
    cells: list[Mark | None] = [None] * BOARD_SIZE
    for cell in line:
        cells[cell] = mark
    return tuple(cells)


@pytest.mark.parametrize("mark", [X, O])
@pytest.mark.parametrize("line", WIN_LINES)
def test_get_winner_detects_every_line(line: tuple[int, int, int], mark: Mark) -> None:
    assert get_winner(board_with_line(line, mark)) is mark


def test_drawn_board_is_draw_without_winner() -> None:
    assert is_draw(DRAWN_BOARD)
    assert get_winner(DRAWN_BOARD) is None


def test_empty_and_partial_boards_are_not_draws() -> None:
    assert not is_draw(EMPTY_BOARD)
    assert not is_draw(place_mark(EMPTY_BOARD, 4, X))


def test_full_board_with_winner_is_not_draw() -> None:
    board: Board = (X, X, X, O, O, X, O, X, O)
    assert get_winner(board) is X
    assert not is_draw(board)


def test_get_next_mark_alternates() -> None:
    assert get_next_mark(EMPTY_BOARD) is X
    assert get_next_mark(place_mark(EMPTY_BOARD, 0, X)) is O


@pytest.mark.parametrize("cell", [-1, BOARD_SIZE])
def test_place_mark_rejects_cell_outside_board(cell: int) -> None:
    with pytest.raises(IllegalMoveError):
        place_mark(EMPTY_BOARD, cell, X)


def test_place_mark_rejects_occupied_cell() -> None:
    board = place_mark(EMPTY_BOARD, 0, X)
    with pytest.raises(IllegalMoveError):
        place_mark(board, 0, O)


def test_place_mark_rejects_wrong_turn() -> None:
    with pytest.raises(IllegalMoveError):
        place_mark(EMPTY_BOARD, 0, O)


def test_place_mark_rejects_move_after_win() -> None:
    with pytest.raises(IllegalMoveError):
        place_mark(X_WON_BOARD, 8, O)


def test_place_mark_does_not_mutate_input() -> None:
    board = place_mark(EMPTY_BOARD, 0, X)
    snapshot = tuple(board)
    new_board = place_mark(board, 1, O)
    assert board == snapshot
    assert new_board[1] is O
    assert EMPTY_BOARD == (None,) * BOARD_SIZE


def test_list_legal_moves_on_empty_board() -> None:
    assert list_legal_moves(EMPTY_BOARD) == list(range(BOARD_SIZE))


def test_list_legal_moves_on_partial_board() -> None:
    board = place_mark(place_mark(EMPTY_BOARD, 4, X), 0, O)
    assert list_legal_moves(board) == [1, 2, 3, 5, 6, 7, 8]


def test_list_legal_moves_on_won_board() -> None:
    assert list_legal_moves(X_WON_BOARD) == []
