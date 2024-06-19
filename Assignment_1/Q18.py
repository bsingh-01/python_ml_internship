def is_anagram(str1, str2):
    if len(str1)!= len(str2):
        return False
    if sorted(str1) == sorted(str2):
        return True
    
str1 = str(input("enter string 1: "))
str2 = str(input("enter string 2: "))

if is_anagram(str1, str2):
    print("The two strings are anagrams")
else:
    print("The two strings aren't anagrams")