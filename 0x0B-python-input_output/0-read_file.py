#!/usr/bin/python3
"""Function read_file"""


def read_file(file_name=""):
    """Reads a file and prints to stdout"""
    with open(file_name, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
