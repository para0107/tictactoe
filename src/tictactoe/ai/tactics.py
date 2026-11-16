import random

from src.tictactoe.core.board import Board
from src.tictactoe.core.mark import Mark
from src.tictactoe.core.rules import get_winner, list_legal_moves, mark_cell


def choose_random_move(board: Board, rng: random.Random) -> int:
    """Return a random legal cell."""
    return rng.choice(list_legal_moves(board))


def _find_winning_move(board: Board, mark: Mark) -> int | None:
    """Return a cell where placing the mark wins, if there is one."""
    for cell in list_legal_moves(board):
        candidate = mark_cell(board, cell, mark)
        if get_winner(candidate) is mark:
            return cell
    return None


def choose_tactical_move(board: Board, mark: Mark, rng: random.Random) -> int:
    """Win if possible, else block the opponent's win, else play randomly."""
    for player in (mark, mark.opponent):
        cell = _find_winning_move(board, player)
        if cell is not None:
            return cell
    return choose_random_move(board, rng)
