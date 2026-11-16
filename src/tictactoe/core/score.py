from dataclasses import dataclass

from src.tictactoe.core.mark import Mark


@dataclass
class Score:
    """Session tally of wins and draws."""

    x_wins: int = 0
    o_wins: int = 0
    draws: int = 0

    def record_result(self, winner: Mark | None) -> None:
        """Count a finished game; None means a draw."""
        if winner is Mark.X:
            self.x_wins += 1
        elif winner is Mark.O:
            self.o_wins += 1
        else:
            self.draws += 1
