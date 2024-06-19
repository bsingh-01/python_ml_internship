# 22. Write a python program that returns the minimum and maximum values 
# in a list of numbers

def find_min_max(numbers):
    if not numbers:
        min_value = min(numbers)
        max_value = max(numbers)
        return min_value, max_value

# Example usage
numbers = input("enter numbers in a list[] with commas: ")
min_value, max_value = find_min_max(numbers)

print("The minimum value is:", min_value)
print("The maximum value is:", max_value)
