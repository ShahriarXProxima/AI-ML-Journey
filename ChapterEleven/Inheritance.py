class Employee:
    company = "DriveTrain Technologies"
    name = ""
    salary = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(
            f"The name of the employee is {self.name}, his salay is {self.salary} and the company is {self.company}"
        )


class Programmer(Employee):
    company = "Therap BD Ltd"

    def __init__(self, name, salary):
        super().__init__(name, salary)


shahriar = Employee("Shahriar", 20000)
shahriar.show()

tahmid = Programmer("Tahmid", 120000)
tahmid.show()
