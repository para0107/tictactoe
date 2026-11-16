from enum import StrEnum


class Mark(StrEnum):
    """A player's mark."""

    X = "X"
    O = "O"

    @property
    def opponent(self) -> "Mark":
        """Return the other mark."""
        return Mark.O if self is Mark.X else Mark.X
