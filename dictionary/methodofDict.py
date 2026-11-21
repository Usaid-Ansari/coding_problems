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