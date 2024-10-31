# Class is blue-print for creating an object-
class Employee:
    language = "Java" # This is a class attribute
    salary = 4200000


aakash = Employee()
aakash.name = "Aakash" # This is an instance attribute
print(aakash.name, aakash.language, aakash.salary)

print("-------------------------------------------------------------")

hitesh = Employee()
hitesh.name = "Hitesh"
print(hitesh.name, hitesh.salary, hitesh.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class