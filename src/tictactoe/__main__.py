import random

from src.tictactoe.cli.session import play_session


def main() -> None:
    """Run the game, exiting quietly on Ctrl-C or end of input."""
    try:
        play_session(input, print, random.Random())
    except (KeyboardInterrupt, EOFError):
        print()


if __name__ == "__main__":
    main()
