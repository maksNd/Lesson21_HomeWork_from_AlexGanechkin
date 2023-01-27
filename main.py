from classes import Request
from utils import create_vaults, report


def main():
    from_vault = None
    to_vault = None
    vaults = create_vaults()  # создаем склады и магазины и наполняем их товарами

    print("Добро пожаловать, властелин логистики!")
    print("Введи количество и наименование товара, откуда и куда его доставить.\n"
          "Пример запроса: доставить 3 коровы из склад1 в магазин1.\n"
          f"Наша сеть МАНГИТ содержит следующие точки: {vaults}\n\n"
          "Итак, начнем! (Чтобы остановиться, введи стоп-слово: анделиверабл)\n", "-" * 20)

    while True:
        query = input()
        if query == "анделиверабл":
            break

        request = Request(vaults, query)

        if None in [request.otkuda, request.to]:
            print("Не задан один из пунктов: отправления или доставки - повторите запрос")
            continue

        for vault in vaults:
            if request.otkuda == vault.__repr__():
                from_vault = vault
            if request.to == vault.__repr__():
                to_vault = vault

        if None in [from_vault, to_vault]:
            print("Нет такого магазина и/или склада в сети МАНГИТ")
            continue

        if request.product not in from_vault.items.keys():
            print(f"Отсутствует на {from_vault}, попробуйте заказать другой товар")
            continue

        if from_vault.items[request.product] < request.amount:
            print(f"Не хватает на {from_vault}, попробуйте заказать меньше")
            continue

        if request.amount > to_vault.get_free_space():
            print(f"В {to_vault} недостаточно места, попробуйте что то другое")
            continue

        if 'магазин' in to_vault.__repr__():
            if request.product not in to_vault.items.keys():
                if to_vault.get_unique_items_count() == to_vault.items_limit:
                    print(f"Достигнут максимальный лимит по ассортименту товаров в {to_vault}")
                    continue

        from_vault.remove(request.product, request.amount)
        to_vault.add(request.product, request.amount)

        report(from_vault, to_vault, request)


if __name__ == "__main__":
    main()
