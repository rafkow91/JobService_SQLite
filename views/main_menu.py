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

class ChangePassword(AbstractView):
    LABEL = 'Zmień swoje hasło'

    def draw(self):
        pass
        


class MainMenu(AbstractView):
    OPTIONS = {
        # Menagers
        1: {
            1: AddWorktime(),
            2: CheckWorktime(),
            3: AddEmployee(),
            4: EditEmployee(),
            5: ShowAllEmployees(),
            9: ChangePassword(),
            0: QuitProgram()
        },
        # Employees
        2: {
            1: AddWorktime(),
            2: CheckWorktime(),
            3: ShowAllEmployees(),
            9: ChangePassword(),
            0: QuitProgram()
        },
        # Practise
        3: {
            1: AddWorktime(),
            2: CheckWorktime(),
            9: ChangePassword(),
            0: QuitProgram()
        },
        # # Calulate salary
        # 4: {
        #     1: CalculateSalary(),
        #     9: ChangePassword(),
        #     0: QuitProgram()
        # }
    }

    def draw(self, group_id):
        system('clear')
        self.draw_logo('Menu główne')

        self.options = MainMenu.OPTIONS[group_id]

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
