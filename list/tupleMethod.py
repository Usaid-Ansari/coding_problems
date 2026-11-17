thistuple = ("apple", "banana", "cherry")
print(type(thistuple))
print(thistuple[1])
a = (1, )
print(type(a))

numbers = (10, 20, 10, 30, 10, 40)
print(numbers.count(10))
print(numbers.index(10))
print("Max number present in tuple : ", max(numbers))
print("Min number present in tuple : ", min(numbers))
print("Sum of all number present in tuple : ", sum(numbers))
print("All the element present in tuple in the Sorted form : ", sorted(numbers))

# Operation in Tuple 
# Accessing elements
n = (10, 20, 30, 40)
print(n)
print(n[0])
print(n[2])

# Slicing
num = (10, 20, 30, 40, 50)
print(num[1:4])
print(num[:3])
print(num[::-1])

# Concatenation = combine the two tuples
a = (10, 20, 30)
b = (40, 50)
print("Concatenate = ", a + b)

# Repetition = Repeat the tuples
repeat = (10, 20)
print(repeat * 3)

# Quick practice
data  = (5, 10, 5, 20, 5, 30)
print(data.count(5))
print(data.index(20))