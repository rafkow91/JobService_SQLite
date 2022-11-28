from time import sleep

from getpass import getpass

from repositories.employees import TitleRepository, EmployeeRepository
from views.abstract_view import AbstractView
from config import EMAIL_DOMAIN
from other_functions import clear_screen, hash_password, print_table


class AddEmployee(AbstractView):
    LABEL = 'Dodawanie nowego pracownika'

    def draw(self):
        clear_screen()
        self.draw_logo(self.LABEL)

    def get_choice(self, option: int = None):
        while True:
            choice = input('Chcesz dodać nowego pracownika? [T/n] ')

            if choice != '' and choice[0].lower() not in ('t', 'y'):
                break

            person = self.create(EMAIL_DOMAIN)
            repository = EmployeeRepository()
            repository.add_new_employee(person)
            self.draw()
            print(f'Poprawnie dodano nowego pracownika ({person["login"]})')
            sleep(1)
            self.draw()

        return False

    def create(self, EMAIL_DOMAIN):
        person = dict()
        person['first_name'] = input('Imię: ')
        person['last_name'] = input('Nazwisko: ')

        while True:
            try:
                person['phone'] = int(input('Nr tel.: '))
            except ValueError:
                print('Numer telefonu musi być ciągiem liczb...')
                continue
            break

        person['login'] = person['first_name'][0].lower() + person['last_name'].lower()
        person['mail'] = person['login'] + '@' + EMAIL_DOMAIN
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
                    print('Lista dostępnych stanowisk:')
                    print(repository.get_titles_list())
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
        title = dict()
        title['name'] = title_name
        while True:
            try:
                title['salary'] = float(input('Wynagrodzenie podstawowe: '))
            except ValueError:
                print('Podana wartość nie jest liczbą. Podaj ponownie')
                continue
            break
        while True:
            try:
                title['group_id'] = int(input('Grupa dostępu: '))
            except ValueError:
                print('Podana wartość nie jest liczbą. Podaj ponownie')
                continue
            break

        return title


class EditEmployee(AbstractView):
    LABEL = 'Edycja konta pracownika'
    repository = EmployeeRepository()

    def draw(self):
        self.draw_logo(EditEmployee.LABEL)

    def get_choice(self):
        clear_screen()
        self.draw()
        print('\t\tLista pracowników:')
        table = [('Id', 'Imię', 'Nazwisko', 'Email', 'Stanowisko')]
        index = self.repository.index()
        table += index

        print_table(table)

        employee_ids = [item[0] for item in index]

        while True:
            try:
                choice = input(
                    'Którego pracownika chcesz edytować? (podaj id) // aby anulować wciśnij "enter" //  ')
                if choice == '':
                    return False
                if int(choice) not in employee_ids:
                    raise ValueError
            except ValueError:
                print('Id musi być liczbą z piewszej kolumny!!')
                continue
            self.edit(int(choice))
            input()
            break
        return False

    def edit(self, employee_id: int):
        clear_screen()
        self.draw()
        print('// aby nie zmieniać danego pola wciśnij "enter"//\n\n')
        existed_employee = self.repository.get_employee_by_id(employee_id)
        print(existed_employee)
        change_employee = []

        # TODO: Tu skończyłem pracować (2022-11-28 21:05)
        for field in existed_employee:
            to_append = input('...')


class ShowAllEmployees(AbstractView):
    LABEL = 'Wyświetlanie wszystkich pracowników'
    repository = EmployeeRepository()

    def draw(self):
        self.draw_logo(ShowAllEmployees.LABEL)

    def get_choice(self):
        clear_screen()
        self.draw()
        table = [('Id', 'Imię', 'Nazwisko', 'Email', 'Stanowisko')]
        table += self.repository.index()

        print_table(table)

        input('\n\n-- Wciśnij dowolny klawisz aby wrócić do menu --\n')

        return False
