from views.abstract_view import AbstractView


class AddEmployee(AbstractView):
    LABEL = 'Dodawanie nowego pracownika'
    
    def draw(self):
        self.draw_logo(AddEmployee.LABEL)

class EditEmployee(AbstractView):
    LABEL = 'Edycja konta pracownika'
    
    def draw(self):
        self.draw_logo(EditEmployee.LABEL)

class ShowAllEmployees(AbstractView):
    LABEL = 'Wyświetlanie wszystkich pracowników'
    
    def draw(self):
        self.draw_logo(ShowAllEmployees.LABEL)