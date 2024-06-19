# 3. Write a python program that calculates the factorial of a given number.
a=int(input("enter a non negative number: "))
result=1
for i in range(1, a+1):
    result *= i

print("the factorial of the given number is: ", result)