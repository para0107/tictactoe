from src.tictactoe.core.mark import Mark

Board = tuple[Mark | None, ...]

BOARD_SIZE = 9
EMPTY_BOARD: Board = (None,) * BOARD_SIZE
WIN_LINES: tuple[tuple[int, int, int], ...] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)
