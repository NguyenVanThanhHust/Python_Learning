import os

def identity(f):
    print("This is f: ", f.__name__)
    return f
    
# this is how to use decorator
@identity
def print_input(input):
    print("This is input: ", input)
    return input
    
if __name__ == "__main__":
    print_input("String")