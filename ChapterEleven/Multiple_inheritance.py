class Employee:
    company =""
    name =""
    
    def __init__(self, name, company):
        self.name = name
        self.company = company
        
    def show(self):
            print(f"The name of the employee is {self.name} and the company is {self.company}")
            

class Coder:
    language = ""
    
    def __init__(self, language):
          self.language= language
          
    def printLanguage(self):
        print(f"The language is {self.language}")      
        

class Programmer(Employee, Coder):
    def __init__(self, language, company):
         super().__init__(language, company)  # python cannot handle the multi-inherited constractor    
         
    def printInfo(self):
        print(f"The name of the employee uses {self.language}, the name of the comapany is {self.company}")
        
        
shahriar= Programmer("Shahriar", "Therap BD")
shahriar.printInfo()        