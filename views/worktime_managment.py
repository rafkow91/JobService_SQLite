from datetime import datetime
from time import sleep
from other_functions import clear_screen

from views.abstract_view import AbstractView
from repositories import WorktimeRepository


class AddWorktime(AbstractView):
    LABEL = 'Uzupełnianie czasu pracy'
    OPTIONS = {
        1: 'dodaj czas wejścia do pracy',
        2: 'dodaj czas wyjścia z pracy',
        0: 'wróć do poprzedniego menu'
    }

    def draw(self):
        clear_screen()
        self.options = AddWorktime.OPTIONS

        self.draw_logo(AddWorktime.LABEL)
        print('Chcesz podać godzinę przyjścia czy wyjścia z pracy?\n')
        for shortcut, descrition in self.options.items():
            print(shortcut, '-', descrition)
        print()

    def get_choice(self):
        option = None

        while option not in self.options:
            try:
                option = int(input('Wybór: '))
            except:
                continue

        if option == 1:
            self.input_start_time()
        elif option == 2:
            self.input_end_time()
        elif option == 0:
            return False

    def input_start_time(self):
        clear_screen()
        MethodLABEL = 'Czas wejścia'
        self.draw_logo(MethodLABEL)
        repository = WorktimeRepository(self.employee_id)

        worktime_date = None
        worktime_time = None

        while True:
            option = input('Chcesz dodać godziny z innej daty? [t/N] ').lower()
            if option == 't':
                while True:
                    try:
                        worktime_date = datetime.strptime(
                            input('Data: [DD-MM-RRRR] '), '%d-%m-%Y').date()
                    except:
                        print('podano niepoprawną datę!!')
                        continue
                    break
                break
            elif option == 'n'or option == '':
                worktime_date = datetime.now().date()
                break
            else:
                print('Wybierz t lub n!')
                continue

        worktime_end_time = repository.get_end_time(worktime_date)
        if worktime_end_time[0] is None:
            worktime_end_time = datetime.strptime('23:59:59', '%H:%M:%S').time()
        else:
            worktime_end_time = datetime.strptime(worktime_end_time[0], '%H:%M:%S').time()

        while True:
            try:
                worktime_time = datetime.strptime(input('Godzina wejścia [HH:MM] '), '%H:%M').time()
                if worktime_time > worktime_end_time:
                    print(
                        f'Godzina zakończenia pracy jest wcześniejsza niż godzina rozpoczęcia!!\nWpisana godzina zakończenia: {worktime_end_time}')
                    sleep(2)
                    continue
            except:
                print('podano niepoprawną godzinę!!')
                continue
            break

        worktime_time = str(worktime_time)

        if repository.get_workday(worktime_date) is None:
            repository.add_workday(worktime_date)

        repository.add_start_time(worktime_date, worktime_time)

    def input_end_time(self):
        clear_screen()
        MethodLABEL = 'Czas wyjścia'
        self.draw_logo(MethodLABEL)
        repository = WorktimeRepository(self.employee_id)

        worktime_date = None
        worktime_time = None

        while True:
            option = input('Chcesz dodać godziny z innej daty? [t/N]').lower()
            if option == 't':
                while True:
                    try:
                        worktime_date = datetime.strptime(
                            input('Data: [DD-MM-RRRR] '), '%d-%m-%Y').date()
                    except:
                        print('podano niepoprawną datę!!')
                        continue
                    break
                break
            elif option == 'n' or option == '':
                worktime_date = datetime.now().date()
                break
            else:
                print('Wybierz t lub n!')
                continue

        worktime_start_time = repository.get_start_time(worktime_date)
        if worktime_start_time[0] is None:
            worktime_start_time = datetime.strptime('00:00:00', '%H:%M:%S').time()
        else:
            worktime_start_time = datetime.strptime(worktime_start_time[0], '%H:%M:%S').time()

        while True:
            try:
                worktime_time = datetime.strptime(input('Godzina wejścia [HH:MM] '), '%H:%M').time()
                if worktime_time < worktime_start_time:
                    print(
                        f'Godzina rozpoczęcia pracy jest późniejsza niż godzina zakończenia!!\nWpisana godzina rozpoczęcia: {worktime_start_time}')
                    sleep(2)
                    continue
            except:
                print('podano niepoprawną godzinę!!')
                continue
            break

        worktime_time = str(worktime_time)

        if repository.get_workday(worktime_date) is None:
            repository.add_workday(worktime_date)

        repository.add_end_time(worktime_date, worktime_time)


class CheckWorktime(AbstractView):
    LABEL = 'Kontrola czasu pracy'
    OPTIONS = {
        1: 'wyświetl dzisiejszy dzień',
        2: 'wyświetl aktualny miesiąc',
        3: 'wyświetl dowolny miesiąc',
        0: 'wróć do poprzedniego menu'
    }

    def draw(self):
        clear_screen()
        self.options = CheckWorktime.OPTIONS

        self.draw_logo(CheckWorktime.LABEL)
        print('Co chcesz wyświetlić?\n')
        for shortcut, descrition in self.options.items():
            print(shortcut, '-', descrition)
        print()

    def get_choice(self, option: int = None):
        while option not in self.options:
            try:
                option = int(input('Wybór: '))
            except:
                continue

        if option == 1:
            self.show_current_day()
        elif option == 2:
            self.show_current_month()
        elif option == 3:
            self.show_month()
        elif option == 0:
            return False

    def show_current_day(self):
        clear_screen()
        MethodLABEL = 'Czas pracy'
        self.draw_logo(MethodLABEL)

        repository = WorktimeRepository(self.employee_id)

        workday = str(datetime.now().date())

        current_day = repository.get_workday(workday)

        try:
            repository.print_worktime([current_day, ])
        except TypeError:
            print('Dziś jeszcze nie wprowadzono godzin!')
            sleep(2)

    def show_current_month(self):
        clear_screen()
        MethodLABEL = 'Czas pracy'
        self.draw_logo(MethodLABEL)

        repository = WorktimeRepository(self.employee_id)

        workmonth = datetime.now().month
        workyear = datetime.now().year

        current_month = repository.get_month(workyear, workmonth)

        repository.print_worktime(current_month)

    def show_month(self):
        clear_screen()
        MethodLABEL = 'Czas pracy'
        self.draw_logo(MethodLABEL)

        repository = WorktimeRepository(self.employee_id)

        print('Podaj rok i miesiąc, który chcesz zobaczyć')

        while True:
            try:
                workyear = int(input('Podaj rok: '))
                if workyear > datetime.now().year or workyear < 1900:
                    raise Exception
                break
            except Exception:
                print(f'Podano błędny rok! Podaj rok z zakresu (1901 - {datetime.now().year})')
                continue

        while True:
            try:
                workmonth = int(input('Podaj miesiąc: '))
                if workmonth > 12 or workmonth < 1:
                    raise Exception
                break
            except Exception:
                print('Podano błędny miesiąc!')
                continue

        month = repository.get_month(workyear, workmonth)
        repository.print_worktime(month)
