#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = sentence if sentence else None
    return len(sentence), first_char
