class Student:
    name = ""
    id= ""
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    @staticmethod # static method decorator
    def hello():
        print("python is a shit")    
        
        
s = Student("shahriar", "242-35-799")
s.hello()        