# Standard libs
from os import system
from time import sleep
# Project's modules
from views.abstract_view import AbstractView
from views.manage_employees import AddEmployee, EditEmployee, ShowAllEmployees
from views.worktime_managment import AddWorktime, CheckWorktime


class QuitProgram(AbstractView):
    LABEL = 'Zamknij program'

    def draw(self):
        system('clear')
        self.draw_logo('Do zobaczenia')
        sleep(1)
        system('clear')
        quit()


class MainMenu(AbstractView):
    OPTIONS = {
        99999: {
            1: AddWorktime(),
            2: CheckWorktime(),
            3: AddEmployee(),
            4: EditEmployee(),
            5: ShowAllEmployees(),
            0: QuitProgram()
        }
    }

    def draw(self, title_id):
        system('clear')
        self.draw_logo('Menu główne')

        self.options = MainMenu.OPTIONS[title_id]

        print('Wybierz co chcesz zrobić:\n')

        for shorcut, option in self.options.items():
            print(shorcut, '-', option.LABEL.lower())
        print()

    def get_choice(self):
        option = None

        while option not in self.options:
            try:
                option = int(input('Wybór: '))
            except:
                continue

        return self.options[option]
