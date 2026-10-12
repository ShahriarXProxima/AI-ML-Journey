class User:
    username =""
    __password=""
    
    def __init__(self, username, password):
        self.username = username
        self.__password = password # "__" makes the atttribute private
        
    def __hello(): # private method  
        print("Hello World")    
        


user = User("shahriarXproxima", "i love bangladesh")
print(user.__password)  # hides the password attribute