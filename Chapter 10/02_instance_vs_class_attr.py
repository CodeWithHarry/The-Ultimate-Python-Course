class Employee: 
    language = "Java" # This is a class attribute
    salary = 1200000


harry = Employee()
harry.language = "JavaScript" # This is an instance attribute takes preference over class variable
print(harry.language, harry.salary)
 