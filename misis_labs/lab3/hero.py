from __future__ import annotations

from enum import Enum

from combat import Combatant, Hit
from core import UnknownCodeError
from item import Armor, Item, ItemCatalog, Weapon
from kit import MageKitFactory, RangerKitFactory, StarterKitFactory, WarriorKitFactory

MAX_NAME_LENGTH = 20
STARTING_GOLD = 50
HEALTH_PER_LEVEL = 15
DAMAGE_PER_LEVEL = 3
EXPERIENCE_PER_LEVEL = 100


class HeroClass(Enum):

    WARRIOR = ("warrior", "Воин", 120, WarriorKitFactory)
    RANGER = ("ranger", "Следопыт", 100, RangerKitFactory)
    MAGE = ("mage", "Маг", 85, MageKitFactory)

    def __init__(self, code: str, display_name: str, base_health: int, kit_factory: type[StarterKitFactory]) -> None:
        self.code = code
        self.display_name = display_name
        self.base_health = base_health
        self._kit_factory = kit_factory

    def starter_kit(self, catalog: ItemCatalog) -> StarterKitFactory:
        return self._kit_factory(catalog)

    @classmethod
    def by_code(cls, code: str) -> HeroClass:
        for hero_class in cls:
            if hero_class.code == code:
                return hero_class

        raise UnknownCodeError("Класс героя", code)


class Hero(Combatant):

    def __init__(self, builder: Hero.Builder) -> None:
        self._name: str = builder.name  # type: ignore[assignment]
        self._hero_class: HeroClass = builder.hero_class  # type: ignore[assignment]
        self._level = builder.level
        self._experience = 0
        self._gold = builder.gold
        self._weapon: Weapon = builder.weapon  # type: ignore[assignment]
        self._armor: Armor = builder.armor  # type: ignore[assignment]
        self._inventory: list[Item] = []
        self._health = self.max_health

    class Builder:

        def __init__(self) -> None:
            self.name: str | None = None
            self.hero_class: HeroClass | None = None
            self.weapon: Weapon | None = None
            self.armor: Armor | None = None
            self.level = 1
            self.gold = STARTING_GOLD

        def set_name(self, name: str) -> Hero.Builder:
            self.name = name
            return self

        def set_hero_class(self, hero_class: HeroClass) -> Hero.Builder:
            self.hero_class = hero_class
            return self

        def set_weapon(self, weapon: Weapon) -> Hero.Builder:
            self.weapon = weapon
            return self

        def set_armor(self, armor: Armor) -> Hero.Builder:
            self.armor = armor
            return self

        def set_starter_kit(self, starter_kit: StarterKitFactory) -> Hero.Builder:
            self.weapon = starter_kit.create_weapon()
            self.armor = starter_kit.create_armor()
            return self

        def set_level(self, level: int) -> Hero.Builder:
            self.level = level
            return self

        def set_gold(self, gold: int) -> Hero.Builder:
            self.gold = gold
            return self

        def build(self) -> Hero:
            if self.name is None or not self.name.strip():
                raise ValueError("У героя должно быть имя")
            if len(self.name) > MAX_NAME_LENGTH:
                raise ValueError(f"Имя героя не может быть длиннее {MAX_NAME_LENGTH} символов")
            if self.hero_class is None:
                raise ValueError("Не выбран класс героя")
            if self.weapon is None or self.armor is None:
                raise ValueError("Герою нужны оружие и броня")
            if self.level < 1:
                raise ValueError("Уровень героя не может быть меньше 1")
            if self.gold < 0:
                raise ValueError("Золота не может быть меньше нуля")

            return Hero(self)

    def roll_damage(self) -> Hit:
        hit = self._weapon.roll_damage()
        return Hit(hit.damage + (self._level - 1) * DAMAGE_PER_LEVEL, hit.critical)

    def receive_hit(self, damage: int) -> int:
        reduced_damage = round(damage * (1 - self._armor.defense))
        dealt = max(1, reduced_damage)
        self._health = max(0, self._health - dealt)
        return dealt

    def is_alive(self) -> bool:
        return self._health > 0

    def restore_health(self) -> None:
        self._health = self.max_health

    def gain_experience(self, amount: int) -> int:
        self._experience += amount
        levels_gained = 0
        while self._experience >= self.experience_to_next_level:
            self._experience -= self.experience_to_next_level
            self._level += 1
            levels_gained += 1

        return levels_gained

    def add_gold(self, amount: int) -> None:
        self._gold += amount

    def spend_gold(self, amount: int) -> None:
        if amount > self._gold:
            raise ValueError(f"Не хватает золота: нужно {amount}, есть {self._gold}")

        self._gold -= amount

    def add_item(self, item: Item) -> None:
        self._inventory.append(item)

    def remove_item(self, item: Item) -> None:
        if item not in self._inventory:
            raise ValueError(f"В инвентаре нет предмета {item.name}")

        self._inventory.remove(item)

    def equip(self, item: Item) -> None:
        if isinstance(item, Weapon):
            self.remove_item(item)
            self._inventory.append(self._weapon)
            self._weapon = item
        elif isinstance(item, Armor):
            self.remove_item(item)
            self._inventory.append(self._armor)
            self._armor = item
        else:
            raise ValueError(f"Предмет нельзя экипировать: {item.name}")

    @property
    def code(self) -> str:
        return self._hero_class.code

    @property
    def name(self) -> str:
        return self._name

    @property
    def health(self) -> int:
        return self._health

    @property
    def max_health(self) -> int:
        return self._hero_class.base_health + (self._level - 1) * HEALTH_PER_LEVEL

    @property
    def hero_class(self) -> HeroClass:
        return self._hero_class

    @property
    def level(self) -> int:
        return self._level

    @property
    def experience(self) -> int:
        return self._experience

    @property
    def experience_to_next_level(self) -> int:
        return self._level * EXPERIENCE_PER_LEVEL

    @property
    def gold(self) -> int:
        return self._gold

    @property
    def weapon(self) -> Weapon:
        return self._weapon

    @property
    def armor(self) -> Armor:
        return self._armor

    @property
    def inventory(self) -> tuple[Item, ...]:
        return tuple(self._inventory)
