# Dictionary is a type of data structure in python which is used for storing elements in ley value format
employee = {
    "name": "Rohan",
    "age": 23,
    "role": "developer",
    "languages known": ["English", "Odia", "Hindi", "Bengali"]
}

print(employee)
print("Employee role:", employee["role"])
print("Languages known by employee:", employee["languages known"])

# Adding a new key and it's value in dictionary

employee["city"] = "Hyderabad"
print(employee)
