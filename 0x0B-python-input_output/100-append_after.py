#!/usr/bin/python3
"""Function append_after"""


def append_after(file_name="", p_search_tring="", p_new_string=""):
    """A function that inserts a line of text to a file"""
    with open(file_name, "r") as f:
        text = f.readlines()

    with open(file_name, "w") as fo:
        s = ""
        for line in text:
            s += line
            if p_search_tring in line:
                s += p_new_string
        fo.write(s)
