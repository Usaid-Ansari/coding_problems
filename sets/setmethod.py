# s = {1, 5, 32, 54, 5, 5, "Harry"}
# print(s)

# set1 = {"banana", "apple", "mango", "cherry"}
# print("banana" in set1)
# print("jamun" in set1)

# set method
# add method
# set2 = {1, 4, 3, 2, 25, 25, 71}
# set2.add(5)
# print(set2)

# update method 
# set3 = {1, 10, 4, 6, 8}
# set3.update([2, 3, 15, 7])
# print(set3)

# remove method
# set4 = {10, 1, 50, 70, 30}
# set4.remove(70)
# print(set4)
  
# discard method  (Removes element safely.) Note:No error if not found
# set5 = {10, 1, 50, 70, 30}
# set5.discard(1000)
# print(set5)

# union method (Combines two sets or more sets)
# a = {1, 2, 3}
# b = {3, 4, 5}
# c = {6, 7, 8}
# print(a.union(b, c))

# Join a Set and a Tuple
# x = {"a", "b", "c"}
# y = (1, 2, 3)
# print(x.union(y))
# x.update(y)
# print(x)

# Use & to find a common element in two sets
set6 = {"apple", "banana", "cherry"}
set7 = {"google", "microsoft", "apple"}
set8 = set6 & set7 
print(set8)

# practice 
a = {10, 20, 30, 40}
b = {20, 40, 50, 60}

print(a & b)
print(a - b)
print(a ^ b) 