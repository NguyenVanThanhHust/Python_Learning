import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
    

def create_fake_data():
    with open("data_test/random_bytes", "a") as source:
        content = randomString(1024)
        source.write(content)
        source.write('\n')
        
if __name__ == '__main__':
    for i in range(1000):
        create_fake_data()