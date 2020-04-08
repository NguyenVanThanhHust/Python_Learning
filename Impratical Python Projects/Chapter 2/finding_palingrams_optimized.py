import os
import sys

from load_dictionary import load_file
    
file_name = "12dicts-6.0.2/American/2of12.txt"
text = load_file(file_name)
    
def get_list_panlidrome():
    global text
    list_word = text
    set_word = set(list_word)
    result = list()
    for word in set_word:
        if len(word) == 1: #skip word like: a, b,..
            continue
        reversed_word = word[::-1]
        for i in range(len(word)):
            first_part = word[:i]
            second_part = word[i:]
            
            if first_part[::-1] in set_word and second_part[::-1] == second_part :
                pair = word + "_" + first_part[::-1]
                result.append(pair)
            if second_part[::-1] in set_word and first_part[::-1] == first_part:
                pair = word + "_" + second_part[::-1]
                result.append(pair)
    return result

if __name__ == "__main__":
    file_name = "12dicts-6.0.2/American/2of12.txt"
    text = load_file(file_name)
    list_panlidrome = get_list_panlidrome()
    print(list_panlidrome)