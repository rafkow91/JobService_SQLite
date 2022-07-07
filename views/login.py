from getpass import getpass
from sqlite3 import connect
from time import sleep

from other_functions import clear_screen, hash_password
from repositories import DB_URL
from views.abstract_view import AbstractView


class LoginMenu(AbstractView):
    def input_login_password(self) -> tuple:
        login = input('Login: ').lower()
        password = getpass('Hasło: ')

        return (login, password)

    def login_user(self) -> tuple:
        clear_screen()
        self.draw_logo('Logowanie')
        data = self.input_login_password()
        connection = connect(DB_URL)
        cursor = connection.cursor()

        cursor.execute(
            '''
                SELECT
                e.password, 
                t.group_id,
                e.id 
            FROM employees e
            left JOIN titles t ON t.id = e.title_id 
            WHERE login like ? 
            ''',
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
