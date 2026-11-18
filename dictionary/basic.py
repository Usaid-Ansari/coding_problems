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