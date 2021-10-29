# standard libs
from os import system
from time import sleep
# project's modules
from views.login import LoginMenu
from views.main_menu import MainMenu


class Application:
    def main(self):
        # Logowanie
        menu = LoginMenu()

        login_validation = (False, 0)

        while not login_validation[0]:

            login_validation = menu.login_user()
            system('clear')

            if login_validation[0]:
                print('\n\nZalogowano poprawnie')
                sleep(1)
                break
            else:
                print('\n\nNiepoprawne dane logowania.. spróbuj jeszcze raz..')
                sleep(1)

    # Menu główne
        title_id = login_validation[1]
        while True:
            menu = MainMenu()
            menu.draw(title_id)
            menu = menu.get_choice()

    # Menu czynności
            while True:
                menu.add_employee_id(login_validation[2])
                menu.draw()
                choice = menu.get_choice()
                if choice == False:
                    break


if __name__ == '__main__':
    app = Application()
    app.main()
