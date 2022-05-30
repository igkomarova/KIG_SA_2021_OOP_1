from utils.welcome import *
from utils.choice import *


if __name__ == '__main__':
    start()
    row_b = 1
    choose_cat(row_b)

    status = False
    print('Оплатить - 0 или продолжить покупки - 1 ')
    while status == False:
        ans = input('>>> ')
        try:
            ans = int(ans)
            if ans == 0:
                save_order()
                status = True
            elif ans == 1:
                row_b += 1
                choose_cat(row_b)
                print('Оплатить - 0 или продолжить покупки - 1 ')
            else:
                print(Fore.LIGHTRED_EX + 'Некорректный ввод', end=' ')
        except ValueError:
            print(Fore.LIGHTRED_EX + 'Некорректный ввод', end=' ')