import math

num = int(input("Enter the number\n"))
sum = 0
while num > 0:
    lastNum = num % 10
    sum += lastNum
    num //= 10

print(math.floor(sum))
