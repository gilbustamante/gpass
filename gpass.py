"""Generates passwords and store them with user-defined keys"""
import random
import string
import argparse

def setup_argparse():
    """Setup and parse arguments"""
    parser = argparse.ArgumentParser(
        prog="GPass",
        description="Generate secure passwords, and store them for easy \
        retrieval")
    parser.add_argument("-l",
                        metavar="Password length",
                        dest="length",
                        type=int,
                        help="The desired length of your password.")
    args = parser.parse_args()
    return args

def generate_pass(length):
    """Generate password with given length"""
    try:
        length = int(length)
    except ValueError:
        print('You must input a number!')
        return 1
    chars = (string.ascii_letters +
             string.digits +
             string.punctuation +
             ' ')
    password = ''.join(random.choices(chars, k=length))
    return password

if __name__ == '__main__':
    args = setup_argparse()
    print(generate_pass(args.length))
