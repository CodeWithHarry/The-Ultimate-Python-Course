letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

# print(letter.replace("<|Name|>", "Harry").replace("<|Date|", "24 September 2050"))
var1=str(input("Enter the name here: "))
var2=str(input("Enter the date here: "))
print("Dear ",var1, "\nYou are selected!\n",var2)