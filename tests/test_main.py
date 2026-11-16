import pytest

from src.tictactoe.__main__ import main


def test_main_returns_on_end_of_input(monkeypatch: pytest.MonkeyPatch) -> None:
    def raise_eof(_: str = "") -> str:
        raise EOFError

    monkeypatch.setattr("builtins.input", raise_eof)
    main()
