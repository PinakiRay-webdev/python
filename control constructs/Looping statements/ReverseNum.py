num = int(input("Enter the number\n"))
reversedNum = ""
while num > 0:
    lastDigit = num % 10
    reversedNum += str(lastDigit)
    num //= 10

print("The reversed number is "+reversedNum)
