from __future__ import annotations

import random
from typing import Sequence, TypeVar

T = TypeVar("T")


class Dice:

    _instance: Dice | None = None
    _random: random.Random

    def __new__(cls) -> Dice:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._random = random.Random()

        return cls._instance

    def reseed(self, seed: int) -> None:
        self._random.seed(seed)

    def next_seed(self) -> int:
        return self._random.randrange(1_000_000)

    def roll(self, low: int, high: int) -> int:
        return self._random.randint(low, high)

    def chance(self, probability: float) -> bool:
        return self._random.random() < probability

    def pick(self, options: Sequence[T]) -> T:
        return self._random.choice(options)


class UnknownCodeError(LookupError):

    def __init__(self, what: str, code: str) -> None:
        super().__init__(f"{what} с кодом '{code}' не существует")
