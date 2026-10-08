class Employee:
    name = "Shahriar"
    language = "Py"
    salary = 1200000
    
    def __init__(self, name, language, salary): # constractro of the object
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getInfo(self):  # "self" works like "this" keyword in Java
        print(f"The name is {self.name} and language is {self.language}")


# tahmid = Employee()
# tahmid.getInfo()

# print(tahmid.name, tahmid.salary)

shahriar = Employee("shahriar", "java", 7000)
print(shahriar.language, shahriar.salary, shahriar.name)