# string are immutable
name = "Usaid"
print(len(name))
nameShort = name[0: 4]
print(nameShort)
charcter1 = name[1]
print(charcter1)
print(name[-4: -1])
print(name[1: 4])

print(name[: 4])  # is same as print(name[0: 4])
print(name[1: ])  # is same as print(name[1: 5])

# Slicing with skip value
word = "amazing"
print(word[1: 6: 3])

