# GPass
Simple password generator tool that generates passwords by pulling random
characters including punctuation and spaces (unless `-a` flag is used).

## Requirements
Python v3 or later

## Usage
`python gpass.py [-h] [-a] [-l length]`

| Option | Description                                               |
|--------|-----------------------------------------------------------|
| `-l`   | Desired length of password (E.g. `-l 15`). Default is 10. |
| `-a`   | Generate password with only alphanumeric characters.      |
| `-h`   | Usage information                                         |

## To Do
* Securely store passwords for later retrieval?
