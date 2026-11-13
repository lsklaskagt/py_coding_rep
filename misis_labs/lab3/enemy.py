from abc import abstractmethod

from combat import Combatant, Hit
from core import Dice

SKELETON_RESISTANCE = 0.3
DRAGON_RESISTANCE = 0.25
FIRE_BREATH_CHANCE = 0.25
FIRE_BREATH_MULTIPLIER = 2


class Enemy(Combatant):

    @property
    @abstractmethod
    def experience_reward(self) -> int: ...

    @abstractmethod
    def roll_gold_reward(self) -> int: ...


class AbstractEnemy(Enemy):

    def __init__(
        self, code: str, name: str, max_health: int,
        min_damage: int, max_damage: int,
        experience_reward: int, gold_reward: int,
    ) -> None:
        self._code = code
        self._name = name
        self._max_health = max_health
        self._min_damage = min_damage
        self._max_damage = max_damage
        self._experience_reward = experience_reward
        self._gold_reward = gold_reward
        self._health = max_health

    def roll_damage(self) -> Hit:
        return Hit(Dice().roll(self._min_damage, self._max_damage), False)

    def receive_hit(self, damage: int) -> int:
        dealt = max(1, self._reduce_damage(damage))
        self._health = max(0, self._health - dealt)
        return dealt

    def _reduce_damage(self, damage: int) -> int:
        return damage

    def is_alive(self) -> bool:
        return self._health > 0

    def roll_gold_reward(self) -> int:
        return Dice().roll(self._gold_reward // 2, self._gold_reward)

    @property
    def experience_reward(self) -> int:
        return self._experience_reward

    @property
    def code(self) -> str:
        return self._code

    @property
    def name(self) -> str:
        return self._name

    @property
    def health(self) -> int:
        return self._health

    @property
    def max_health(self) -> int:
        return self._max_health


class Goblin(AbstractEnemy):

    def __init__(self) -> None:
        super().__init__("goblin", "Гоблин", 50, 6, 14, 40, 30)


class Skeleton(AbstractEnemy):

    def __init__(self) -> None:
        super().__init__("skeleton", "Скелет", 110, 10, 24, 90, 70)

    def _reduce_damage(self, damage: int) -> int:
        return round(damage * (1 - SKELETON_RESISTANCE))


class Dragon(AbstractEnemy):

    def __init__(self) -> None:
        super().__init__("dragon", "Дракон", 260, 16, 22, 500, 400)

    def roll_damage(self) -> Hit:
        bite = super().roll_damage()
        if Dice().chance(FIRE_BREATH_CHANCE):
            return Hit(bite.damage * FIRE_BREATH_MULTIPLIER, True)

        return bite

    def _reduce_damage(self, damage: int) -> int:
        return round(damage * (1 - DRAGON_RESISTANCE))
