# Using walrus operator - This will allow user to concisely write the code without it writing in multiple line-
if (n := len([1, 2, 3, 4, 5, 6])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 
    # Output: List is too long (5 elements, expected <= 3)

print("----------------------------------------------------------------------------------------------")

# We can import these to make it the list or any other type of data.
from typing import List, Union, Tuple 

# List of integers 
numbers: List[int] = [1, 2, 3, 4, 5] 
 
# Tuple of a string and an integer 
person: Tuple[str, int] = ("Alice", 30) 
 
# Dictionary with string keys and integer values 
scores: dict[str, int] = {"Alice": 90, "Bob": 85} 
 
# Union type for variables that can hold multiple types 
identifier: Union[int, str] = "ID123" 
identifier = 12345  # Also valid
n : int = 18

print("----------------------------------------------------------------------------------------------")


name: str = "Aakash"


def  sum(a: int, b: int) -> int:
    return a+b

print(sum(4,18))

print("----------------------------------------------------------------------------------------------")

def http_status(status): 
    match status:  
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status"  


print(http_status(5007))

print("----------------------------------------------------------------------------------------------")

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyy")
    print(v)
    
except Exception as e:
    print(e) 

print("Thank You")

print("----------------------------------------------------------------------------------------------")

a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is {a/b}")
    
print("----------------------------------------------------------------------------------------------")

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 


else:
    print("I am inside else")


print("----------------------------------------------------------------------------------------------")
def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally")


main()

print("----------------------------------------------------------------------------------------------")

a = 89

def fun(): 
    # global a
    a = 3
    print(a)


fun()
print(a)

print("----------------------------------------------------------------------------------------------")

l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

print("----------------------------------------------------------------------------------------------")

myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)