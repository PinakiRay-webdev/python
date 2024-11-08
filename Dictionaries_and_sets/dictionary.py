# Dictionary is a type of data structure in python which is used for storing elements in ley value format
employee = {
    "name": "Rohan",
    "age": 23,
    "role": "developer",
    "languages known": ["English", "Odia", "Hindi", "Bengali"]
}

# to get the particular key we can write :
    # 1-> dictionary_name["key"]
    # 2-> dictionary_name.get("key")

#The first one is not recomended because that will throw error in case if the key is not present. The second will give null value if the key is not present. So that our rest of the code can continue with out any interuption


print(employee)
print("Employee role:", employee.get("role"))
print("Languages known by employee:", employee["languages known"])

# Adding a new key and it's value in dictionary

employee["city"] = "Hyderabad"
print(employee)

print("=================")
# Major Methods in dictionaries
print(employee.keys())      # return all keys
print(employee.values())    # return all values
print(employee.items())     # Returns all (key , value) pairs as tuple

print(employee.update({"Date of birth": "15th june 2001"}))     # updates the dictionary by taking a new dic
print(employee)