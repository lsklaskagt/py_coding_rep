from __future__ import annotations

from typing import Sequence

from camp import Merchant
from combat import Outcome
from console_view import ConsoleView
from hero import Hero, HeroClass
from item import (
    CHAINMAIL,
    ELVEN_BOW,
    EMBER_STAFF,
    IRON_SWORD,
    PLATE_ARMOR,
    Item,
    ItemCatalog,
    create_default_catalog,
)
from world import Crypt, DragonLair, Forest, LocationRegistry

VIEW = ConsoleView()


def main() -> None:
    catalog = create_default_catalog()
    locations = LocationRegistry([
        Forest(catalog),
        Crypt(catalog),
        DragonLair(catalog),
    ])
    merchant = Merchant(catalog, [
        IRON_SWORD, ELVEN_BOW, EMBER_STAFF, CHAINMAIL, PLATE_ARMOR,
    ])

    hero = create_hero(catalog)
    print(f"{hero.name} разбивает лагерь на опушке мистического леса.")

    while True:
        print()
        VIEW.print_hero(hero)
        print("1 - отправиться в экспедицию, 2 - снаряжение, 3 - торговец, 0 - выйти из игры")
        choice = input().strip()
        if choice == "1":
            go_on_expedition(hero, locations)
        elif choice == "2":
            manage_equipment(hero)
        elif choice == "3":
            visit_merchant(hero, merchant)
        elif choice == "0":
            return
        else:
            print("Такого варианта нет")


def create_hero(catalog: ItemCatalog) -> Hero:
    print("Создайте своего героя!")
    while True:
        print("Выберите класс:")
        hero_classes = list(HeroClass)
        for i, hero_class in enumerate(hero_classes):
            kit = hero_class.starter_kit(catalog)
            print(
                f"{i + 1} - {hero_class.display_name} (здоровье {hero_class.base_health}): "
                f"{VIEW.describe(kit.create_weapon())}, {VIEW.describe(kit.create_armor())}"
            )
        class_index = read_choice(len(hero_classes))
        if class_index < 0:
            continue
        hero_class = hero_classes[class_index]

        print("Введите имя:")
        name = input().strip()

        try:
            return (
                Hero.Builder()
                .set_name(name)
                .set_hero_class(hero_class)
                .set_starter_kit(hero_class.starter_kit(catalog))
                .build()
            )
        except ValueError as error:
            print(f"Не получилось создать героя: {error}")


def go_on_expedition(hero: Hero, locations: LocationRegistry) -> None:
    all_locations = locations.all
    print("Куда отправимся?")
    for i, location in enumerate(all_locations):
        print(f"{i + 1} - {location.display_name} (рекомендуемый уровень {location.recommended_level})")
    index = read_choice(len(all_locations))
    if index < 0:
        return

    location = all_locations[index]
    report = location.explore(hero)
    print()
    VIEW.print_report(report, location.display_name)

    if report.battle.outcome == Outcome.VICTORY and location.code == DragonLair.CODE:
        print(f"\nДракон повержен! Барды еще долго будут петь о подвиге героя по имени {hero.name}.")


def manage_equipment(hero: Hero) -> None:
    inventory = hero.inventory
    if not inventory:
        print("Инвентарь пуст")
        return

    print("Что экипировать? (0 - назад)")
    print_items(inventory)
    index = read_choice(len(inventory))
    if index < 0:
        return

    item = inventory[index]
    hero.equip(item)
    print("Экипировано: " + VIEW.describe(item))


def visit_merchant(hero: Hero, merchant: Merchant) -> None:
    print(f'Торговец: "Чего желаешь?" (золото: {hero.gold})')
    print("1 - купить, 2 - продать, 0 - назад")
    choice = input().strip()
    if choice == "1":
        buy(hero, merchant)
    elif choice == "2":
        sell(hero, merchant)


def buy(hero: Hero, merchant: Merchant) -> None:
    showcase = merchant.showcase
    for i, item in enumerate(showcase):
        print(f"{i + 1} - {VIEW.describe(item)}: {item.price} золота")
    index = read_choice(len(showcase))
    if index < 0:
        return

    try:
        item = merchant.buy(hero, showcase[index].code)
        print("Куплено: " + VIEW.describe(item))
    except ValueError as error:
        print(error)


def sell(hero: Hero, merchant: Merchant) -> None:
    inventory = hero.inventory
    if not inventory:
        print("Продавать нечего (экипированные предметы продать нельзя)")
        return

    for i, item in enumerate(inventory):
        print(f"{i + 1} - {VIEW.describe(item)}: {merchant.sell_price(item)} золота")
    index = read_choice(len(inventory))
    if index < 0:
        return

    item = inventory[index]
    price = merchant.sell(hero, item)
    print(f"Продано: {item.name} за {price} золота")


def print_items(items: Sequence[Item]) -> None:
    for i, item in enumerate(items):
        print(f"{i + 1} - {VIEW.describe(item)}")


def read_choice(count: int) -> int:
    try:
        choice = int(input().strip())
        if 1 <= choice <= count:
            return choice - 1
    except ValueError:
        pass

    return -1


if __name__ == "__main__":
    main()
