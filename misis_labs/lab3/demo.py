from __future__ import annotations

from console_view import ConsoleView
from core import Dice
from hero import Hero, HeroClass
from item import FIERY, IRON_SWORD, create_default_catalog
from world import Crypt, Forest


def main() -> None:
    catalog = create_default_catalog()
    view = ConsoleView()

    print("===== Одиночка =====")
    first = Dice()
    second = Dice()
    print(f"Dice() возвращает один и тот же объект: {first is second}")

    print()
    print("===== Прототип =====")
    plain_sword = catalog.create(IRON_SWORD)
    fiery_sword = catalog.create(IRON_SWORD)
    fiery_sword.enchant(FIERY)
    print("Первая копия:        " + view.describe(plain_sword))
    print("Вторая копия:        " + view.describe(fiery_sword))
    print("Новая копия шаблона: " + view.describe(catalog.create(IRON_SWORD)))
    print(f"Копии - разные объекты: {plain_sword is not fiery_sword}")

    print()
    print("===== Абстрактная фабрика =====")
    for hero_class in HeroClass:
        kit = hero_class.starter_kit(catalog)
        print(
            f"{hero_class.display_name}: {view.describe(kit.create_weapon())}, "
            f"{view.describe(kit.create_armor())}"
        )

    print()
    print("===== Строитель =====")
    hero = (
        Hero.Builder()
        .set_name("Артурчик")
        .set_hero_class(HeroClass.WARRIOR)
        .set_starter_kit(HeroClass.WARRIOR.starter_kit(catalog))
        .set_level(2)
        .build()
    )
    view.print_hero(hero)
    try:
        (
            Hero.Builder()
            .set_hero_class(HeroClass.MAGE)
            .set_starter_kit(HeroClass.MAGE.starter_kit(catalog))
            .build()
        )
    except ValueError as error:
        print(f"Герой без имени не создается: {error}")
    try:
        Hero.Builder().set_name("Мерлин").build()
    except ValueError as error:
        print(f"Герой без класса не создается: {error}")

    print()
    print("===== Фабричный метод =====")
    forest = Forest(catalog)
    crypt = Crypt(catalog)
    view.print_report(forest.explore(hero, 7), forest.display_name)
    print()
    view.print_report(crypt.explore(hero, 7), crypt.display_name)


if __name__ == "__main__":
    main()
