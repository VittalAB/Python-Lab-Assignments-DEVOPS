class Employee:

    def __init__(self, name, pay):
        self._name = name
        self._pay = pay
        self._email = self._name + "@gmail.com"
    
    @property
    def name(self):
        return self._name
