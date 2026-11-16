import random

from src.tictactoe.ai.difficulty import Difficulty
from src.tictactoe.ai.minimax import choose_best_move
from src.tictactoe.ai.tactics import choose_random_move, choose_tactical_move
from src.tictactoe.core.board import Board
from src.tictactoe.core.mark import Mark


def choose_move(board: Board, mark: Mark, difficulty: Difficulty, rng: random.Random) -> int:
    """Return the computer's cell for the given difficulty."""
    if difficulty is Difficulty.EASY:
        return choose_random_move(board, rng)
    if difficulty is Difficulty.MEDIUM:
        return choose_tactical_move(board, mark, rng)
    return choose_best_move(board, mark)
