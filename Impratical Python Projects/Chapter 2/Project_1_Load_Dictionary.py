import os
import sys

def load_file(filename):
    """
    Load text file as a list
    Arguments:
    - text filename
    
    Exceptions:
    - IOException if filename not found
    
    Returns:
    - A list fo all words in a text file in lower case
    """
    try:
        with open(filename) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{} \n Error opening {}. Terminal program".format(e, filename), filename=sys.stderr)
        sys.exit(1)
        
if __name__ == "__main__":
    file_name = "Sample_text.txt"
    text = load_file(file_name)
    print(text)                                                   