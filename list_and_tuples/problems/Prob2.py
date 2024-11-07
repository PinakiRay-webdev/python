# write a program in python to check if a list contains palindrome elements or not
myList = [1, 2, 3, 2, 1]

copyList = myList.copy()
copyList.reverse()

if copyList == myList:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
