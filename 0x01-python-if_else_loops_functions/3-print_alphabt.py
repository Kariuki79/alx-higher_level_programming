#!/usr/bin/python3
''' a program that prints the
ASCII alphabet, in lowercase,
not followed by a new line '''

for letter in range(97, 123):
     if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
