#!/usr/bin/python3
def uppercase(str):
    for h in str:
        if 97 <= ord(h) <= 122:
            h = chr(ord(h) - 32)
        print("{:s}".format(h), end="")
    print("")
