import random

from src.tictactoe.ai.computer import choose_move
from src.tictactoe.ai.difficulty import Difficulty
from src.tictactoe.cli import messages
from src.tictactoe.cli.prompts import (
    Mode,
    ReadLine,
    WriteLine,
    read_cell,
    read_difficulty,
    read_mode,
    read_rematch,
)
from src.tictactoe.cli.render import render_board, render_score
from src.tictactoe.core.board import EMPTY_BOARD
from src.tictactoe.core.mark import Mark
from src.tictactoe.core.rules import (
    IllegalMoveError,
    get_next_mark,
    get_winner,
    is_draw,
    place_mark,
)
from src.tictactoe.core.score import Score

_COMPUTER_MARK = Mark.O


def play_game(
    read_line: ReadLine,
    write_line: WriteLine,
    computer_difficulty: Difficulty | None,
    rng: random.Random,
) -> Mark | None:
    """Play one game with X first and return the winner, or None for a draw."""
    board = EMPTY_BOARD
    while get_winner(board) is None and not is_draw(board):
        write_line(render_board(board))
        mark = get_next_mark(board)
        if computer_difficulty is not None and mark is _COMPUTER_MARK:
            cell = choose_move(board, mark, computer_difficulty, rng)
            write_line(messages.COMPUTER_MOVE.format(mark=mark, cell=cell + 1))
            board = place_mark(board, cell, mark)
            continue
        try:
            board = place_mark(board, read_cell(read_line, write_line, mark), mark)
        except IllegalMoveError:
            write_line(messages.CELL_OCCUPIED)
    write_line(render_board(board))
    winner = get_winner(board)
    write_line(messages.DRAW if winner is None else messages.WIN.format(mark=winner))
    return winner


def play_session(read_line: ReadLine, write_line: WriteLine, rng: random.Random) -> None:
    """Play games until the players decline a rematch, keeping the score."""
    computer_difficulty = None
    if read_mode(read_line, write_line) is Mode.VS_COMPUTER:
        computer_difficulty = read_difficulty(read_line, write_line)
    score = Score()
    while True:
        score.record_result(play_game(read_line, write_line, computer_difficulty, rng))
        write_line(render_score(score))
        if not read_rematch(read_line):
            break
    write_line(messages.GOODBYE)
