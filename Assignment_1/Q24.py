'''Q 24. Write a program that acts as a simple calculator. It should take two numbers and 
an operator (+, -, *, /) as input and print the result. '''

num1 = int(input("enter the 1st no. : "))
num2 = int(input("enter the 2nd no. : "))
operator = input("choose an operator out of {+, -, *, /}: ")

if operator == "+":
    result = (num1 + num2)
elif operator == "-":
    result = (num1 - num2)
elif operator == "*":
    result = (num1 * num2)
else: result = (num1 // num2 )

print("the output is: ", result)