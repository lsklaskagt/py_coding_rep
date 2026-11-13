from __future__ import annotations

import copy
from abc import ABC, abstractmethod
from dataclasses import dataclass

from combat import Hit
from core import Dice, UnknownCodeError

CRITICAL_MULTIPLIER = 2
MAX_DEFENSE = 0.75


@dataclass(frozen=True)
class Enchantment:
    code: str
    name: str
    bonus_damage: int
    bonus_defense: float
    bonus_price: int


SHARP = Enchantment("sharp", "Острое", 3, 0, 20)
FIERY = Enchantment("fiery", "Огненное", 6, 0, 50)
STURDY = Enchantment("sturdy", "Прочное", 0, 0.05, 20)
WARDING = Enchantment("warding", "Охранное", 0, 0.10, 50)

FOR_WEAPONS = (SHARP, FIERY)
FOR_ARMOR = (STURDY, WARDING)


class Item(ABC):

    def __init__(self, code: str, name: str, base_price: int) -> None:
        self._code = code
        self._name = name
        self._base_price = base_price
        self._enchantments: list[Enchantment] = []

    def copy(self) -> Item:
        clone = copy.copy(self)
        clone._enchantments = list(self._enchantments)
        return clone

    @property
    @abstractmethod
    def possible_enchantments(self) -> tuple[Enchantment, ...]: ...

    @property
    @abstractmethod
    def description(self) -> str: ...

    def enchant(self, enchantment: Enchantment) -> None:
        if enchantment not in self.possible_enchantments:
            raise ValueError(f"Зачарование '{enchantment.name}' не подходит для предмета '{self._name}'")

        self._enchantments.append(enchantment)

    @property
    def code(self) -> str:
        return self._code

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> int:
        return self._base_price + sum(enchantment.bonus_price for enchantment in self._enchantments)

    @property
    def enchantments(self) -> tuple[Enchantment, ...]:
        return tuple(self._enchantments)


class Weapon(Item):

    def __init__(self, code: str, name: str, base_price: int, damage: int) -> None:
        super().__init__(code, name, base_price)
        self._damage = damage

    @abstractmethod
    def roll_damage(self) -> Hit: ...

    @property
    def damage(self) -> int:
        return self._damage + sum(enchantment.bonus_damage for enchantment in self.enchantments)

    @property
    def possible_enchantments(self) -> tuple[Enchantment, ...]:
        return FOR_WEAPONS


class Sword(Weapon):

    def roll_damage(self) -> Hit:
        return Hit(self.damage, False)

    @property
    def description(self) -> str:
        return f"урон {self.damage}"


class Bow(Weapon):

    def __init__(self, code: str, name: str, base_price: int, damage: int, critical_chance: float) -> None:
        super().__init__(code, name, base_price, damage)
        self._critical_chance = critical_chance

    def roll_damage(self) -> Hit:
        if Dice().chance(self._critical_chance):
            return Hit(self.damage * CRITICAL_MULTIPLIER, True)

        return Hit(self.damage, False)

    @property
    def description(self) -> str:
        return f"урон {self.damage}, шанс крита {round(self._critical_chance * 100)}%"


class Staff(Weapon):

    def __init__(self, code: str, name: str, base_price: int, damage: int, scatter: float) -> None:
        super().__init__(code, name, base_price, damage)
        self._scatter = scatter

    def roll_damage(self) -> Hit:
        return Hit(Dice().roll(self._min_damage, self._max_damage), False)

    @property
    def description(self) -> str:
        return f"урон {self._min_damage}-{self._max_damage}"

    @property
    def _min_damage(self) -> int:
        return round(self.damage * (1 - self._scatter))

    @property
    def _max_damage(self) -> int:
        return round(self.damage * (1 + self._scatter))


class Armor(Item):

    def __init__(self, code: str, name: str, base_price: int, defense: float) -> None:
        super().__init__(code, name, base_price)
        self._defense = defense

    @property
    def defense(self) -> float:
        total = self._defense + sum(enchantment.bonus_defense for enchantment in self.enchantments)
        return min(total, MAX_DEFENSE)

    @property
    def possible_enchantments(self) -> tuple[Enchantment, ...]:
        return FOR_ARMOR

    @property
    def description(self) -> str:
        return f"защита {round(self.defense * 100)}%"


class ItemCatalog:

    def __init__(self) -> None:
        self._prototypes: dict[str, Item] = {}

    def register(self, prototype: Item) -> None:
        self._prototypes[prototype.code] = prototype

    def create(self, code: str) -> Item:
        prototype = self._prototypes.get(code)
        if prototype is None:
            raise UnknownCodeError("Предмет", code)

        return prototype.copy()

    def create_weapon(self, code: str) -> Weapon:
        item = self.create(code)
        if isinstance(item, Weapon):
            return item

        raise ValueError(f"Предмет '{code}' не является оружием")

    def create_armor(self, code: str) -> Armor:
        item = self.create(code)
        if isinstance(item, Armor):
            return item

        raise ValueError(f"Предмет '{code}' не является броней")

    @property
    def codes(self) -> list[str]:
        return list(self._prototypes)


TRAINING_SWORD = "training-sword"
HUNTING_BOW = "hunting-bow"
APPRENTICE_STAFF = "apprentice-staff"
CHAINMAIL = "chainmail"
LEATHER_ARMOR = "leather-armor"
LINEN_ROBE = "linen-robe"

IRON_SWORD = "iron-sword"
ELVEN_BOW = "elven-bow"
EMBER_STAFF = "ember-staff"
PLATE_ARMOR = "plate-armor"

GOBLIN_CLEAVER = "goblin-cleaver"
BONE_BOW = "bone-bow"
NECROMANCER_STAFF = "necromancer-staff"
KNIGHT_BLADE = "knight-blade"
CRYPT_MAIL = "crypt-mail"
DAWN_BLADE = "dawn-blade"
DRAGONSCALE_ARMOR = "dragonscale-armor"


def create_default_catalog() -> ItemCatalog:
    catalog = ItemCatalog()

    catalog.register(Sword(TRAINING_SWORD, "Тренировочный меч", 20, 12))
    catalog.register(Bow(HUNTING_BOW, "Охотничий лук", 20, 10, 0.3))
    catalog.register(Staff(APPRENTICE_STAFF, "Посох ученика", 20, 14, 0.3))
    catalog.register(Armor(CHAINMAIL, "Кольчуга", 40, 0.3))
    catalog.register(Armor(LEATHER_ARMOR, "Кожаная броня", 30, 0.2))
    catalog.register(Armor(LINEN_ROBE, "Льняная роба", 15, 0.1))

    catalog.register(Sword(IRON_SWORD, "Железный меч", 80, 17))
    catalog.register(Bow(ELVEN_BOW, "Эльфийский лук", 90, 14, 0.4))
    catalog.register(Staff(EMBER_STAFF, "Тлеющий посох", 90, 20, 0.3))
    catalog.register(Armor(PLATE_ARMOR, "Латы", 120, 0.4))

    catalog.register(Sword(GOBLIN_CLEAVER, "Гоблинский тесак", 40, 15))
    catalog.register(Bow(BONE_BOW, "Костяной лук", 140, 17, 0.4))
    catalog.register(Staff(NECROMANCER_STAFF, "Посох некроманта", 150, 25, 0.35))
    catalog.register(Sword(KNIGHT_BLADE, "Клинок рыцаря", 150, 23))
    catalog.register(Armor(CRYPT_MAIL, "Кольчуга стража склепа", 160, 0.45))
    catalog.register(Sword(DAWN_BLADE, "Клинок рассвета", 500, 35))
    catalog.register(Armor(DRAGONSCALE_ARMOR, "Драконья чешуя", 500, 0.55))

    return catalog
