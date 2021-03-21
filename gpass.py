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
                        default=10,
                        help="The desired length of your password.")
    parser.add_argument("-a",
                        action="store_true",
                        dest="alphanumeric",
                        help="Generates a password containing only \
                        alphanumeric values")
    args = parser.parse_args()
    return args


def generate_pass(length):
    """Generate default password with given length"""
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


def generate_alphanumeric_pass(length):
    """Generate alphanumeric password with given length"""
    try:
        length = int(length)
    except ValueError:
        print('You must input a number!')
        return 1
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choices(chars, k=length))
    return password


if __name__ == '__main__':
    given_args = setup_argparse()
    if given_args.alphanumeric:
        print(generate_alphanumeric_pass(given_args.length))
    else:
        print(generate_pass(given_args.length))
