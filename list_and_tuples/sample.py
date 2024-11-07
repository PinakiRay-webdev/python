# List in python.
# List is mutable
marks = [45, 50, 34, 48, 39]
fruits = ["Manfo", "Banana", "Apple"]

# In list we can store different types of data types
random = [12, "Rohan", 45.3, True]
print(marks)
print(fruits)

# Properties of the list
print(fruits[2])    # Accessing an element from it's index
print("The length og thr fruits list is:", len(fruits))     # getting the length of the list
fruits.append("Dragon fruit")    # Appending an element
print(fruits)
fruits.insert(2, "Kiwi")    # to add element in the list at a particular index
print(fruits)
print(marks[1:4])   # slicing of a list. (1st one is included and 2nd one is excluded
marks.sort()    # to sort the list in ascending order
print(marks)
marks.sort(reverse=True)    # to sort the list in descending order
print(marks)


