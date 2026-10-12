class Employee:
    company = ""
    name = ""

    def __init__(self, name, company):
        self.name = name
        self.company = company

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


shahriar = Employee("shahriar", "Therap")

print(shahriar.name)
shahriar.name="tahmid"
print(shahriar.name)
