# Standard libs
from datetime import datetime
from os import system
from time import sleep
# Project's modules
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
        system('clear')
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
            self.add_end_time()
        elif option == 0:
            return False

    def input_start_time(self):
        system('clear')
        MethodLABEL = 'Czas wejścia'
        self.draw_logo(MethodLABEL)
        repository = WorktimeRepository(self.employee_id)
        
        worktime_date = None
        worktime_time = None
        
        while True:
            try:
                worktime_date = datetime.strptime(input('Data: [DD-MM-RRRR] '), '%d-%m-%Y').date()
            except:
                print('podano niepoprawną datę!!')
                continue
            break
        
        while True:
            try:
                worktime_time = datetime.strptime(input('Godzina wejścia [HH:MM] '), '%H:%M').time()
            except:
                print('podano niepoprawną godzinę!!')
                continue
            break
        
        worktime_time = str(worktime_time)

        if repository.get_workday(worktime_date) is None:
            repository.add_workday(worktime_date)

        repository.add_start_time(worktime_date, worktime_time)


    def add_end_time(self):
        MethodLABEL = 'Czas wyjścia'
        self.draw_logo(MethodLABEL)
        repository = WorktimeRepository(self.employee_id)
        sleep(10)


class CheckWorktime(AbstractView):
    LABEL = 'Kontrola czasu pracy'

    def draw(self):
        self.draw_logo(CheckWorktime.LABEL)
        repository = WorktimeRepository(self.employee_id)