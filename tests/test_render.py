from src.tictactoe.cli.render import render_board, render_score
from src.tictactoe.core.board import EMPTY_BOARD
from src.tictactoe.core.mark import Mark
from src.tictactoe.core.score import Score


def test_empty_board_shows_all_numbers() -> None:
    text = render_board(EMPTY_BOARD)
    for number in range(1, 10):
        assert str(number) in text


def test_board_shows_marks_instead_of_numbers() -> None:
    board = (Mark.X, None, None, None, Mark.O, None, None, None, None)
    text = render_board(board)
    assert "X" in text and "O" in text
    assert "1" not in text and "5" not in text
    assert "2" in text


def test_score_text() -> None:
    text = render_score(Score(x_wins=2, o_wins=1, draws=3))
    assert text == "Score - X: 2  O: 1  Draws: 3"
