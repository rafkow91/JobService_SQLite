# standard libs
from os import system
from time import sleep
# project modules
from other_functions import hash_password
from views.login import LoginMenu


if __name__ == '__main__':
    menu = LoginMenu()

    login_validation = (False, 0)

    while not login_validation[0]:
        login_validation = menu.login_user()
        system('cls')

        if login_validation[0]:
            print('Zalogowano poprawnie')
            sleep(2)
            break
        else:
            print('Niepoprawne dane logowania.. spróbuj jeszcze raz..')

    system('cls')
    print('Witaj w moim programie!!')
    

