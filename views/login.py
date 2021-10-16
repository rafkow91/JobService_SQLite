# standard libs
from getpass import getpass
from os import system
from time import sleep
# project's modules
from database.db import get_connection
from other_functions import hash_password
from views.abstract_view import AbstractView


class LoginMenu(AbstractView):
    def input_login_password(self) -> tuple:
        login = input('Login: ')
        password = getpass('Hasło: ')

        return (login, password)

    def login_user(self) -> tuple:
        self.draw_logo('Logowanie')
        data = self.input_login_password()
        cursor = get_connection()

        cursor.execute(
            'SELECT password, title_id FROM employees WHERE login like :login',
            {"login": data[0].lower()}
        )

        data_from_db = cursor.fetchone()
        cursor.close()

        try:
            if data_from_db[0] == hash_password(data[1]):
                return (True, data_from_db[1])
        except TypeError:
            print(f'\tBłąd!!\nUżytkownik {data[0]} nie istnieje w bazie pracowników')
            sleep(2)
        return (False, 0)

    def index(self):
        cursor = get_connection()
        cursor.execute(
            'SELECT * FROM employees'
        )
        return cursor.fetchall()
