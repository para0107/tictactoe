from collections.abc import Callable


def scripted(*lines: str) -> Callable[[str], str]:
    answers = iter(lines)
    return lambda _: next(answers)
