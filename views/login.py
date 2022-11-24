from getpass import getpass
from time import sleep

from other_functions import clear_screen, hash_password
from views.abstract_view import AbstractView
from repositories import LoginRepository


class LoginMenu(AbstractView):
    def input_login_password(self) -> tuple:
        login = input('Login: ').lower()
        password = getpass('Hasło: ')

        return (login, password)

    def login_user(self) -> tuple:
        clear_screen()
        self.draw_logo('Logowanie')
        data = self.input_login_password()
        repository = LoginRepository()
        data_from_db = repository.get_data(data[0])

        try:
            if data_from_db[0] == hash_password(data[1]):
                return (True, data_from_db[1], data_from_db[2])
        except TypeError:
            print(f'\tBłąd!!\nUżytkownik {data[0]} nie istnieje w bazie pracowników')
            sleep(2)
        return (False, 0, None)

    def index(self):
        self.cursor.execute(
            'SELECT * FROM employees'
        )
        return self.cursor.fetchall()
