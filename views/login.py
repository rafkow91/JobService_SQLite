# standard libs
from getpass import getpass
from os import system
from sqlite3 import connect
from time import sleep
# project's modules
from other_functions import hash_password
from repositories import DB_URL
from views.abstract_view import AbstractView


class LoginMenu(AbstractView):
    def input_login_password(self) -> tuple:
        login = input('Login: ')
        password = getpass('Hasło: ')

        return (login, password)

    def login_user(self) -> tuple:
        system('clear')
        self.draw_logo('Logowanie')
        data = self.input_login_password()
        connection = connect(DB_URL)
        cursor = connection.cursor()

        cursor.execute(
            'SELECT password, title_id, id FROM employees WHERE login like ?',
            (data[0].lower(),)
        )

        data_from_db = cursor.fetchone()
        cursor.close()

        try:
            if data_from_db[0] == hash_password(data[1]):
                return (True, data_from_db[1], data_from_db[2])
        except TypeError:
            print(f'\tBłąd!!\nUżytkownik {data[0]} nie istnieje w bazie pracowników')
            sleep(2)
        return (False, 0, None)

    def index(self):
        connection = connect(DB_URL)
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM employees'
        )
        return cursor.fetchall()
