'''# 10. Write a python program that converts a given string to uppercase.
input_string = input("enter a string: ")
upper_string = input_string.upper()
print("upper string is: ", upper_string)
'''

# 11. Write a python program that generates the first n numbers in the Fibonacci sequence
def fibonacci(n):
    fib_series = []

    a , b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a , b = b, a+b
    return fib_series

user_input = int(input("enter the number of terms you want to see in fibonacci series: "))
fib_series = fibonacci(user_input)
print("the fibonacci series till", user_input, "is: ", fib_series)