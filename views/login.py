class AbstractView():
    pass


class MainMenu(AbstractView):
    def __init__(self) -> None:
        title = 'Rejestracja czasu pracy'
        print(len(title), '-'*(len(title)+8), '\n', ' '*4, f'{title}\n\nProszę się zalogować do systemu:')

    def input_login_password(self) -> tuple:
        login = input('Login: ')
        password = input('Hasło: ')

        return (login, password)

    def login_user(self) -> bool:
        data = self.input_login_password()
