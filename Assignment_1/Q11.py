'''

13. Write a program that asks the user for their birth year and calculates their age

birth_year= int(input("enter you birth year: "))
current_age = 2024 - birth_year
print("you are", current_age, "years old.",)

if current_age >= 18:
    print("you cool af bro. keep going!")
else:
    print("you're not an adult.")
'''
# 17. Write a program in python that converts a given string to title case (first letter of each word capitalized)

input_string = input("enter a string: ")
output_str = input_string.title()
print("the new string is: ", output_str)


