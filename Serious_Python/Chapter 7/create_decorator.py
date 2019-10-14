import os

def identity(f):
    print("This is f: ", f)
    return f
    
# this is how to use decorator
@identity
def print_input(input):
    print("This is input: ", input)
    
if __name__ == "__main__":
    print("String")