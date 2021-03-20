"""Generates passwords"""
import random
import string

def generate_pass(length):
    """Generate password with given length"""
    try:
        length = int(length)
    except ValueError:
        print('You must input a number!')
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(chars, k=length))
    return password

print(generate_pass(20))
