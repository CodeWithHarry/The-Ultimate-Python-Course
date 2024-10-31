class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    # self is best practice to use you can also use rr, this anything / without self it will give and error 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    # staticmethod annotation is used insted of self - it doesn't need an object
    @staticmethod
    def greet():
        print("Good morning")


aakash = Employee()
# aakash.language = "JavaScript" # This is an instance attribute
aakash.greet()
aakash.getInfo() 
# Employee.getInfo(aakash)
 