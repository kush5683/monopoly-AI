from random import randint


def roll() -> tuple[int, int]:
    return randint(1, 6), randint(1, 6)
