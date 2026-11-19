marks = {
    "Salman": 75,
    "Aaquib": 82,
    "Abrar": 45,
    "colors": ["red", "orange", "green"]
}
print(marks)
print(type(marks))
print(marks["Salman"])
print(len(marks))
print(marks["colors"][2])

# dict() method
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 

# Accesing items
thedict = {
    "brand": "ford",
    "model": "mustang",
    "year": 1987,
}
print(thedict["model"])

# There is also a method called get() that will give you the same result:
x = thedict.get("year")
print(x)

# The keys() method will return a list of all keys in the dictionary
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x) 

# practice
car = {
"brand": "BMW",
"model": "5 series",
"year": 2024,
}

x = car.keys()
print(x) #before the change
car["color"] = "black"
print(x) #after the change

# Change Values
newCar = {
    "brand": "Toyota",
    "model": "Fortuner",
    "year": 2018,
}
newCar["year"] = 2022
print(newCar)

# Update Dictionary
newCar.update({"year": 2021})
print(newCar)

# The pop method remove the item
car1 = {
    "brand": "audi",
    "model": "M7",
    "year": 2023
}
car1.pop("model")
print(car1)