from src.tictactoe.core.board import BOARD_SIZE, WIN_LINES, Board
from src.tictactoe.core.mark import Mark


class IllegalMoveError(ValueError):
    """Raised when a move breaks the rules."""


def get_winner(board: Board) -> Mark | None:
    """Return the mark that completed a line, if any."""
    for first, second, third in WIN_LINES:
        if board[first] is not None and board[first] == board[second] == board[third]:
            return board[first]
    return None


def is_draw(board: Board) -> bool:
    """Return True when the board is full and nobody has won."""
    return None not in board and get_winner(board) is None


def get_next_mark(board: Board) -> Mark:
    """Return the mark that moves next: X first, then alternating."""
    return Mark.X if board.count(Mark.X) == board.count(Mark.O) else Mark.O


def list_legal_moves(board: Board) -> list[int]:
    """Return the empty cells in ascending order, or none once the game is won."""
    if get_winner(board) is not None:
        return []
    return [cell for cell, occupant in enumerate(board) if occupant is None]


def mark_cell(board: Board, cell: int, mark: Mark) -> Board:
    """Return a new board with the mark set on the cell, without checking the rules."""
    return board[:cell] + (mark,) + board[cell + 1 :]


def place_mark(board: Board, cell: int, mark: Mark) -> Board:
    """Return a new board with the mark placed.

    Raises:
        IllegalMoveError: The cell is off the board or taken, the game is over, or it is not
            this mark's turn.
    """
    if not 0 <= cell < BOARD_SIZE:
        raise IllegalMoveError(f"Cell {cell} is outside the board")
    if board[cell] is not None:
        raise IllegalMoveError(f"Cell {cell} is already taken")
    if get_winner(board) is not None:
        raise IllegalMoveError("The game is already over")
    if mark is not get_next_mark(board):
        raise IllegalMoveError(f"It is not {mark}'s turn")
    return mark_cell(board, cell, mark)
