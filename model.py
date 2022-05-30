from utils.welcome import *


class User:
    def __init__(self):
        self.__login = None
        self.__password = None
        self.__order = {}

    def __repr__(self):
        return f'Вы вошли как {self.__login}'

    def add_order(self, order: dict):
        self.__order.update(order)

    def accnt(self, login, password):
        self.__login = login
        self.__password = password


class GoodsCategory:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def __repr__(self):
        return f'{self.__id}. {self.__name}'


class Goods:
    def __init__(self, id, cat, name, price, rating):
        self.__id = id
        self.__cat = cat
        self.__name = name
        self.__price = price
        self.__rating = rating

    def __repr__(self):
        return f'{self.__id}. {self.__cat} {self.__name} - {self.__price} руб., рейтинг: {self.__rating}'

    def change_rating(self):
        pass


class Basket:
    def __init__(self):
        self.__bskt = {}

    def __repr__(self):
        return f'{self.__bskt}'

    def add_item(self, row_b: int, goods: dict):
        self.__bskt.update({row_b: goods})

