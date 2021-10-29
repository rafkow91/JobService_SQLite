from abc import ABC, abstractmethod
from os import system


class AbstractView(ABC):
    def add_employee_id(self, employee_id):
        self.employee_id = employee_id

    def draw():
        pass

    def draw_logo(self, title):
        self.title = title
        self.weight = len(self.title)+35
        print('', '-'*self.weight, '\n |', ' '*15, self.title, ' '*14, '|\n',
              '-'*self.weight, '\n\n')

    def get_choice(self):
        pass

