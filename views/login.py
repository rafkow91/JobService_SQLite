from database.db import get_connection
from other_functions import hash_password


class LoginMenu():
    def __init__(self) -> None:
        title = 'Rejestracja czasu pracy'
        print('-'*(len(title)+8), '\n', ' '*4, f'{title}\n\nProszę się zalogować do systemu:')

    def input_login_password(self) -> tuple:
        login = input('Login: ')
        password = input('Hasło: ')

        return (login, password)

    def login_user(self) -> tuple:
        data = self.input_login_password()
        cursor = get_connection()

        cursor.execute(
            'SELECT password, title_id FROM employees WHERE login like :login',
            {"login": data[0].lower()}
        )

        data_from_db = cursor.fetchone()
        if data_from_db[0] == hash_password(data[1]):
            return (True, data_from_db[1])

        return (False, 0)

    def index(self):
        cursor = get_connection()
        cursor.execute(
            'SELECT * FROM employees'
        )
        return cursor.fetchall()