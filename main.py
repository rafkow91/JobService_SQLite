from views.login import MainMenu


class Application:
    @staticmethod
    def main():
        if not x_login_correct:
            menu = MainMenu()
            menu.login_user()


if __name__ == '__main__':
    x_login_correct = False
    
    Application.main()
