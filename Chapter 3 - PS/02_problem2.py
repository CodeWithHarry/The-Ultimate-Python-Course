letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Aakash").replace("<|Date|>", "20 Oct 2025")) 
# Chaining is happening here