from colorama import *
import os
from model import *
import json
import random

CHARS = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

basket = Basket()
user = User()

def start():

    init(autoreset=True)

    print(30 * '\n')

    clear = lambda: os.system('cls')
    clear()

    print(Fore.YELLOW + '\N{glowing star} Магазин "Сапёр Electronics" \N{glowing star}')
    print()

    answ = answer_proc('Войти в личный кабинет - 0 или зарегистрироваться - 1')
    input_user(answ)


def input_user(answ):
    global user

    with open('users.json', 'r') as j:
        json_users = json.load(j)

    status = False
    while status == False:
        login = input('Введите логин >>> ')
        if answ == 1 and login not in list(json_users):
            print(Fore.GREEN + f'Логин {login} свободен')
            print()
            status = True
        elif answ == 1 and login in list(json_users):
            print(Fore.LIGHTRED_EX + 'Такой логин уже существует')
            answ = answer_proc('Хотите войти с этим логином - 0 или продолжить регистрацию - 1?')
        elif answ == 0 and login not in list(json_users):
            print(Fore.LIGHTRED_EX + 'Такого логина не существует')
            answ = answer_proc('Хотите продолжить ввод учетных данных - 0 или зарегистрироваться - 1?')
        else:
            print(Fore.GREEN + 'Логин корректный')
            print()
            status = True

    status = False
    while status == False:
        password = input('Введите пароль >>> ')
        if answ == 0 and (login, password) in json_users.items():
            print('Пара логин-пароль существует')
            status = True
        elif answ == 0 and (login, password) not in json_users.items():
            print('Пара логин-пароль не существует')
        else:
            if len(password) < 6:
                print(Fore.LIGHTRED_EX + 'Недопустимый пароль')
                check = False
            elif password.isdigit() or (password.isalpha() and password.islower()):
                print(Fore.LIGHTRED_EX + 'Ненадежный пароль')
                check = False
            elif (password.isdigit() and password.lower()) or (password.isalpha() and password.lower()):
                print(Fore.LIGHTRED_EX + 'Слабый пароль')
                check = False
            else:
                print(Fore.GREEN + 'Надежный пароль')
                check = True
            status = True

            if check == False:
                password = gen_password()

            save_user(login, password)

    j.close()

    user.accnt(login, password)
    print(user.__repr__())
    return user


def gen_password(length: int = 8) -> str:
    password = ''
    for i in range(length):
        password += random.choice(CHARS)

    print()
    print(f'Сгенерирован пароль <{password}>. Запомните его или запишите')
    return password


def save_user(login, password):
    with open('users.json', 'r') as j:
        json_users = json.load(j)
        json_users[login] = password

    with open('users.json', 'w') as j:
        json.dump(json_users, j)
    j.close()


def answer_proc(question) -> int:
    print(question, end=' ')
    status = False
    while status == False:
        answ = input('>>> ')
        try:
            answ = int(answ)
            if answ == 0:
                print()
                print(Fore.GREEN + '\N{sparkles}' + ' Вход в личный кабинет ' + '\N{sparkles}')
                status = True
            elif answ == 1:
                print()
                print(Fore.GREEN + '\N{sparkles}' + ' Новый пользователь ' + '\N{sparkles}')
                status = True
            else:
                print(Fore.LIGHTRED_EX + 'Некорректный ввод', end=' ')
        except ValueError:
            print(Fore.LIGHTRED_EX + 'Некорректный ввод', end=' ')
    return answ
