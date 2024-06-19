# 19. Write a python program that removes all punctuation from a given string.
import string

def remove_punctuation(input_string):
    no_punctuation_list = []

    for char in input_string:
        if char not in string.punctuation:
            no_punctuation_list.append(char)
    return