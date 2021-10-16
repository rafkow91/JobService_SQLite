from os import system
from time import sleep
from views.abstract_view import AbstractView


class AddWorktime(AbstractView):
    LABEL = 'Uzupełnianie czasu pracy'
    OPTIONS = {
        1: 'dodaj czas wejścia do pracy',
        2: 'dodaj czas wyjścia z pracy',
        0: 'wróć do poprzedniego menu'
    }
    
    def draw(self):
        system('cls')
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
            self.add_start_time()
        elif option == 2:
            self.add_end_time()
        elif option == 0:
            return False
        
            
    def add_start_time(self):
        MethodLABEL = 'Czas wejścia'
        self.draw_logo(MethodLABEL)
        sleep(10)

    def add_end_time(self):
        MethodLABEL = 'Czas wyjścia'
        self.draw_logo(MethodLABEL)
        sleep(10)

class CheckWorktime(AbstractView):
    LABEL = 'Kontrola czasu pracy'

    def draw(self):
        self.draw_logo(CheckWorktime.LABEL)


