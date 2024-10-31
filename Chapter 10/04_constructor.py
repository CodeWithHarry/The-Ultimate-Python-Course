class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called methods, starting from "__" is called as dunder methods. it is special method.
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


aakash = Employee("Aakash", 1300000, "JavaScript") 
# aakash.name = "aakash"
print(aakash.name, aakash.salary, aakash.language)
aakash.getInfo()
