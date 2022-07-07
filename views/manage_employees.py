from getpass import getpass

from views.abstract_view import AbstractView
from my_secret_file import domain
from repositories import TitleRepository, EmployeeRepository
from other_functions import clear_screen, hash_password


class AddEmployee(AbstractView):
    LABEL = 'Dodawanie nowego pracownika'

    def draw(self):
        clear_screen()
        self.draw_logo(AddEmployee.LABEL)

        person = self.create(domain)
        repository = EmployeeRepository()
        print(person)
        repository.add_new_employee(person)
        input()

    def create(self, domain):
        person = dict()

        person['first_name'] = input('Imię: ')
        person['last_name'] = input('Nazwisko: ')

        while True:
            try:
                person['phone'] = int(input('Nr tel.: '))
            except:
                print('Numer telefonu musi być ciągiem liczb...')
                continue
            break

        person['login'] = person['first_name'][0].lower() + person['last_name'].lower()
        person['mail'] = person['login'] + '@' + domain
        person['title'] = input('Stanowisko: ')

        repository = TitleRepository()
        title_id = repository.get_title_id_by_title(person['title'])

        if title_id is None:
            choice = None
            while choice not in ['t', 'n']:
                choice = input(
                    '''Podane stanowisko nie istnieje.
                    \nWciśnij [t] aby uzupełnić brakujące informacje i utworzyć stanowisko lub [n] aby ponownie podać nazwę stanowiska.
                    \nWybór:\t''').lower()

                if choice == 't':
                    print(person['title'])
                    title = self.create_title(person['title'])
                    repository.add_new_title(title)
                    break

                elif choice == 'n':
                    person['title'] = input('Podaj ponownie nazwę stanowiska: ')
                    break

        repository2 = TitleRepository()
        person['title_id'] = repository2.get_title_id_by_title(person['title'])[0]

        while True:
            password1 = getpass('Hasło: ')
            password2 = getpass('Powtórz hasło: ')

            if password1 == password2:
                person['password'] = hash_password(password1)
                break

            print('Podane hasła się różnią!')

        return person

    @staticmethod
    def create_title(title_name):
        title = {}
        title['name'] = title_name
        while True:
            try:
                title['salary'] = float(input('Wynagrodzenie podstawowe: '))
            except:
                print('Podana wartość nie jest liczbą. Podaj ponownie')
                continue
            break
        while True:
            try:
                title['group_id'] = int(input('Grupa dostępu: '))
            except:
                print('Podana wartość nie jest liczbą. Podaj ponownie')
                continue
            break

        return title

# TODO:
class EditEmployee(AbstractView):
    LABEL = 'Edycja konta pracownika'

    def draw(self):
        self.draw_logo(EditEmployee.LABEL)

# TODO:
class ShowAllEmployees(AbstractView):
    LABEL = 'Wyświetlanie wszystkich pracowników'

    def draw(self):
        self.draw_logo(ShowAllEmployees.LABEL)
