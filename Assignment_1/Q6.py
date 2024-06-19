# Write a program that takes a string input from the user and writes it to a text file
text = (input("enter the text you want to copy: "))
file_path = "C:/Users/Bhavyaa/Downloads/Python projects/python ml internship june 2024/testtext.txt"
with open(file_path, 'w') as file:
    file.write(text)

