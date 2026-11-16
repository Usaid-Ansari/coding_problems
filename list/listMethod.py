# List Method
friends = ["Apple", "Aakash", 7, False, "bunty", "tea"]
print(friends)

friends.append("Usaid")  #append = add last of the index
print(friends)
print(friends.append("usaid"))  # They show none beacsue they not return any value

L1 = [41, 21, 13, 15, 16, 22]
print(L1)
L1.sort()
print("Sorted List : ",L1)
L1.reverse()
print("reverse list : ", L1)
L1.insert(3, 421)
print("Inserted List : ", L1)
L1.pop(2)
print("Popped List : ", L1)
name = ["Rasshad", "Abdullah", "Abdurahman", "Hammad"]
name.sort()
print(name)
name1 = ["Ali", "Ahmed"]
name1.append("Mazin")
print(name1)
numbers = [40, 20, 50, 10, 60]
numbers.sort()
print(numbers)
items = [5, 10, 15, 20]
print(items[2])
print(items[0:3])  # slicing

fruits = ["Mango", "Apple", "Banana"]
# x = fruits.sort()
# print(fruits)
# print(x)

x = sorted(fruits)
print(fruits)
print(x)
fruits.insert(1,"Watermelon")
print(fruits)
fruits.remove("Apple")
print(fruits)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
thislist.pop(2)
print(thislist)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thisList = ["round", "cycle", "toy"]
del thisList[1]
print(thisList)

# The clear() method empties the list.
thislist = ["apple", "banana", "jamun", "orange"]
thislist.clear()
print(thislist)