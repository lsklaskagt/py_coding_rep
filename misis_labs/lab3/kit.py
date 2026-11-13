from abc import ABC, abstractmethod

from item import (
    APPRENTICE_STAFF,
    CHAINMAIL,
    HUNTING_BOW,
    LEATHER_ARMOR,
    LINEN_ROBE,
    TRAINING_SWORD,
    Armor,
    ItemCatalog,
    Weapon,
)


class StarterKitFactory(ABC):

    @abstractmethod
    def create_weapon(self) -> Weapon: ...

    @abstractmethod
    def create_armor(self) -> Armor: ...


class WarriorKitFactory(StarterKitFactory):

    def __init__(self, catalog: ItemCatalog) -> None:
        self._catalog = catalog

    def create_weapon(self) -> Weapon:
        return self._catalog.create_weapon(TRAINING_SWORD)

    def create_armor(self) -> Armor:
        return self._catalog.create_armor(CHAINMAIL)


class RangerKitFactory(StarterKitFactory):

    def __init__(self, catalog: ItemCatalog) -> None:
        self._catalog = catalog

    def create_weapon(self) -> Weapon:
        return self._catalog.create_weapon(HUNTING_BOW)

    def create_armor(self) -> Armor:
        return self._catalog.create_armor(LEATHER_ARMOR)


class MageKitFactory(StarterKitFactory):

    def __init__(self, catalog: ItemCatalog) -> None:
        self._catalog = catalog

    def create_weapon(self) -> Weapon:
        return self._catalog.create_weapon(APPRENTICE_STAFF)

    def create_armor(self) -> Armor:
        return self._catalog.create_armor(LINEN_ROBE)
