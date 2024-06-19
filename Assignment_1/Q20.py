# 20. Write a python program that takes a list of numbers and returns their sum.
num_list = []
input_str = input("Enter the numbers you want to add, separated by spaces: ")
for num in input_str.split():
    num_list.append(float(num))
total_sum = sum(num_list)
print("the sum of the numbers is: ", total_sum)