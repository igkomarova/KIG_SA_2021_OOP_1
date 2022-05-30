from colorama import *
import json
import ast
from model import *
import random
from utils.welcome import basket
from utils.welcome import user

def choose_cat(row_b: int):
    init(autoreset=True)

    status = False

    with open('consumer_electronics.json', 'r', encoding='utf-8') as json_f:
        d = json.load(json_f)
    cats = d["categories"]
    json_f.close()

    print()
    print(Fore.GREEN + '\N{sparkles}' + 'Категории товаров' + '\N{sparkles}')

    category = {}

    for k, v in cats.items():
        category[k] = GoodsCategory(k, v)
        print(category[k].__repr__())


    print('Выберите категорию товаров: ', end='')

    while status == False:
        cat = input('>>> ')
        try:
            answ = int(cat)
            if cat in cats.keys():
                print()
                status = True
            else:
                print(Fore.LIGHTRED_EX + 'Некорректный ввод', end=' ')
        except ValueError:
            print(Fore.LIGHTRED_EX + 'Некорректный ввод', end=' ')

    choose_goods(row_b, cat, cats[cat])


def choose_goods(row_b: int, cat: int, name: str):

    with open('consumer_electronics.json', 'r', encoding='utf-8') as json_f:
        d = json.load(json_f)
    prods = d["producers"]
    json_f.close()

    goods = {}
    print(Fore.GREEN + '\N{sparkles}' + 'Товары категории ' + name + Fore.GREEN + '\N{sparkles}')
    for k, v in prods.items():
        goods[k] = Goods(str(cat)+k, name, v, random.randint(1000, 100000), random.randint(1, 10))
        print(goods[k].__repr__())

    print()
    status = False
    print('Выберите товар из предложенного списка: ', end='')

    while status == False:
        choice = input('>>> ')
        try:
            answ = int(choice)
            if choice in prods.keys():
                print('Вы выбрали -', goods[choice].__repr__())
                status = True
            else:
                print(Fore.LIGHTRED_EX + 'Некорректный ввод', end=' ')
        except ValueError:
            print(Fore.LIGHTRED_EX + 'Некорректный ввод', end=' ')

    buy(row_b, goods[choice].__dict__)

def buy(row_b, goods: dict):
    global basket

    basket.add_item(row_b, goods)

    print()
    print('В корзине')
    print(71*'-')
    print('{:5}|{:6}|{:30}|{:11}|{:7}|{:7}'.format('№', 'Номер', 'Категория', 'Товар', 'Цена', 'Рейтинг'))
    print(71 * '-')
    rows_basket = ast.literal_eval(basket.__repr__())
    for k, v in rows_basket.items():
        print('{:<5}|{:<6}|{:<30}|{:<11}|{:<7}|{:<7}'.format(k, v["_Goods__id"], v["_Goods__cat"], v["_Goods__name"], v["_Goods__price"], v["_Goods__rating"]))
    print()

    return basket

def save_order():
    global user
    global basket

    user.add_order(basket.__dict__)
    print(user.__dict__)

