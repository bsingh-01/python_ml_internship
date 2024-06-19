#2. Write a python program that checks whether a given number is even or odd.
a = int(input("enter a number:"))
test_even = a % 2
if test_even == 0:
    print("the input number is even")
else:
    print("the given number is not even")
