# 26. Write a program in python that checks if a string starts with a given prefix or ends with a given suffix
input_string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")
suffix = input("Enter the suffix to check: ")

starts_with_prefix = input_string.startswith(prefix)

ends_with_suffix = input_string.endswith(suffix)

# results
print(f"String starts with prefix '{prefix}': {starts_with_prefix}")
print(f"String ends with suffix '{suffix}': {ends_with_suffix}")
