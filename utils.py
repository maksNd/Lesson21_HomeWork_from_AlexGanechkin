from classes import Store, Shop

vault_names = ["склад1", "магазин1", "склад2", "магазин2", "магазин3"]
vaults = []
goods = [['склад1', 'печеньки', 10],
         ['склад1', 'собачки', 40],
         ['склад2', 'коробки', 15],
         ['склад2', 'елки', 5]
         ]


def create_vaults():

    for name in vault_names:
        if 'склад' in name:
            vault = Store(name)

            for good in goods:
                if vault.__repr__() == good[0]:
                    vault.add(good[1], good[2])
        else:
            vault = Shop(name)

        vaults.append(vault)

    return vaults


def report(from_vault, to_vault, request):
    print(f"Нужное количество есть на {from_vault}")
    print(f"Курьер забрал {request.amount} {request.product} со {from_vault}")
    print(f"Курьер везет {request.amount} {request.product} со {from_vault} в {to_vault}")
    print(f"Курьер доставил {request.amount} в {to_vault}")
    vault_list(from_vault)
    vault_list(to_vault)

    print("--")


def vault_list(vault):
    print(f"\nВ {vault} хранится:")
    for name, amount in vault.items.items():
        print(f"{amount} {name}")
