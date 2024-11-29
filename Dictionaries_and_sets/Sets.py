# set is a type of data structure which can store unordered unique and immutable items.
# set is a mutable but the elements in the set are immutable

mySet = {1, 2, 3, 4, 5, 1}
print(mySet)    # In the output you can 1 only one time, as it stores unique values. Hence we can't store duplicate values here.

# Another way of declaring sets

myNewSet = set()    # initially it is a null set

# Adding values to the set
myNewSet.add(10)
myNewSet.add(45)
myNewSet.add(3)

print(myNewSet)

