student = {
    "name": "Usaid",
    "age": 22,
    "marks": 82,
    "city": "Dhule",
}
print(student.keys())
print(student.values())
print(student.items())
student.pop("city")
print(student)
print(student.get("marks2"))
student.popitem() # Remove the last element on the dictionary
print(student)
new_student = student.copy() # Copy the dictionary
print(new_student)
student.clear() # Clear the dictionary
print(student)

#Practice Challenge
car = {"brand": "Toyota", "year": 2018}
car.update({"year": 2022})
print(car["year"])
car.pop("brand")
print(car)