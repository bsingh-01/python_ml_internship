# 12. Write a python program that calculates the sum of the digits of a given number.
number = input("Enter a number: ")
sum_of_digits = sum(int(digit) for digit in number)
print("The sum of the digits is:", sum_of_digits)
