from Employee import Employee

class Developer(Employee):

    def __init__(self, name, pay, lang):
        super().__init__(name, pay)
        self._pro_lang = lang

        