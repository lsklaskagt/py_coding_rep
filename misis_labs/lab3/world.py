from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable

from combat import Battle, BattleReport, Outcome
from core import Dice, UnknownCodeError
from enemy import Dragon, Enemy, Goblin, Skeleton
from hero import Hero
from item import (
    BONE_BOW,
    CRYPT_MAIL,
    DAWN_BLADE,
    DRAGONSCALE_ARMOR,
    GOBLIN_CLEAVER,
    HUNTING_BOW,
    KNIGHT_BLADE,
    LEATHER_ARMOR,
    NECROMANCER_STAFF,
    Item,
    ItemCatalog,
)

LOOT_CHANCE = 0.6
ENCHANT_CHANCE = 0.3


@dataclass(frozen=True)
class Rewards:
    experience: int
    gold: int
    loot: Item | None
    levels_gained: int


@dataclass(frozen=True)
class ExpeditionReport:
    seed: int
    location_code: str
    battle: BattleReport
    rewards: Rewards


class Location(ABC):

    def __init__(self, code: str, display_name: str, recommended_level: int, catalog: ItemCatalog) -> None:
        self._code = code
        self._display_name = display_name
        self._recommended_level = recommended_level
        self._catalog = catalog

    @abstractmethod
    def _create_enemy(self) -> Enemy: ...

    @property
    @abstractmethod
    def _loot_table(self) -> tuple[str, ...]: ...

    def explore(self, hero: Hero, seed: int | None = None) -> ExpeditionReport:
        dice = Dice()
        if seed is None:
            seed = dice.next_seed()
        dice.reseed(seed)

        hero.restore_health()
        enemy = self._create_enemy()
        battle = Battle(hero, enemy).run()

        if battle.outcome == Outcome.VICTORY:
            rewards = self._reward(hero, enemy, dice)
        else:
            rewards = self._punish(hero)

        return ExpeditionReport(seed, self._code, battle, rewards)

    def _reward(self, hero: Hero, enemy: Enemy, dice: Dice) -> Rewards:
        experience = enemy.experience_reward
        gold = enemy.roll_gold_reward()
        loot = self._roll_loot(dice)

        levels_gained = hero.gain_experience(experience)
        hero.add_gold(gold)
        if loot is not None:
            hero.add_item(loot)

        return Rewards(experience, gold, loot, levels_gained)

    def _roll_loot(self, dice: Dice) -> Item | None:
        if not dice.chance(LOOT_CHANCE):
            return None

        loot = self._catalog.create(dice.pick(self._loot_table))
        if dice.chance(ENCHANT_CHANCE):
            loot.enchant(dice.pick(loot.possible_enchantments))

        return loot

    def _punish(self, hero: Hero) -> Rewards:
        lost_gold = hero.gold // 2
        hero.spend_gold(lost_gold)
        return Rewards(0, -lost_gold, None, 0)

    @property
    def code(self) -> str:
        return self._code

    @property
    def display_name(self) -> str:
        return self._display_name

    @property
    def recommended_level(self) -> int:
        return self._recommended_level


class Forest(Location):

    CODE = "forest"

    def __init__(self, catalog: ItemCatalog) -> None:
        super().__init__(Forest.CODE, "Мистический лес", 1, catalog)

    def _create_enemy(self) -> Enemy:
        return Goblin()

    @property
    def _loot_table(self) -> tuple[str, ...]:
        return (GOBLIN_CLEAVER, HUNTING_BOW, LEATHER_ARMOR)


class Crypt(Location):

    CODE = "crypt"

    def __init__(self, catalog: ItemCatalog) -> None:
        super().__init__(Crypt.CODE, "Заброшенный склеп", 3, catalog)

    def _create_enemy(self) -> Enemy:
        return Skeleton()

    @property
    def _loot_table(self) -> tuple[str, ...]:
        return (KNIGHT_BLADE, BONE_BOW, NECROMANCER_STAFF, CRYPT_MAIL)


class DragonLair(Location):

    CODE = "dragon-lair"

    def __init__(self, catalog: ItemCatalog) -> None:
        super().__init__(DragonLair.CODE, "Логово дракона", 5, catalog)

    def _create_enemy(self) -> Enemy:
        return Dragon()

    @property
    def _loot_table(self) -> tuple[str, ...]:
        return (DAWN_BLADE, DRAGONSCALE_ARMOR)


class LocationRegistry:

    def __init__(self, locations: Iterable[Location]) -> None:
        self._locations: dict[str, Location] = {}
        for location in locations:
            self._locations[location.code] = location

    def get(self, code: str) -> Location:
        location = self._locations.get(code)
        if location is None:
            raise UnknownCodeError("Локация", code)

        return location

    @property
    def all(self) -> list[Location]:
        return list(self._locations.values())
