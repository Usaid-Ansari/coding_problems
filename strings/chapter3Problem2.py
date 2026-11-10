letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> ''' 

print(letter.replace("<|Name|>", "Usaid").replace("<|Date|>", "20 August"))
print("\n")
print(letter.replace("<|Name|>", "Salman").replace("<|Date|>", "28 April"))