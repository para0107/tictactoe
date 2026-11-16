from src.tictactoe.core.mark import Mark
from src.tictactoe.core.score import Score


def test_record_result_counts_each_outcome() -> None:
    score = Score()
    score.record_result(Mark.X)
    score.record_result(Mark.X)
    score.record_result(Mark.O)
    score.record_result(None)
    assert (score.x_wins, score.o_wins, score.draws) == (2, 1, 1)
