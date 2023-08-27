from Employee import Employee
from Developer import Developer


class Manager(Employee):
    def __init__(self, name, emp=None):
        super().__init__(name, pay=None)
        
        if emp:
            self._employees = emp   
        else:
            self._employees = []
    

    def add_employee(self, emp):
        self._employees.append(emp)
    

    def remove_employee(self, emp):
        self._employees.remove(emp)

    