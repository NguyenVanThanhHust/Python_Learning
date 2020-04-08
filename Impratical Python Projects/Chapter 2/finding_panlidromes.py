import os
import sys

from load_dictionary import load_file
    
def get_list_panlidrome(list_word):
    result = list()
    for word in list_word:
        if word[::-1] == word and len(word) > 1:
            result.append(word)
    return result
if __name__ == "__main__":
    file_name = "12dicts-6.0.2/American/2of12.txt"
    text = load_file(file_name)
    list_panlidrome = get_list_panlidrome(text)
    print(list_panlidrome)