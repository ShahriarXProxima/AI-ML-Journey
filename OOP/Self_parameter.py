class Employee:
    name = "Shahriar"
    language = "Py"
    salary = 1200000

    def getInfo(self):  # "self" works like "this" keyword in Java
        print(f"The name is {self.name} and language is {self.language}")


tahmid = Employee()
print(f"Name: {tahmid.name}")

tahmid.getInfo()
