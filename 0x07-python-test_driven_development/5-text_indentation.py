#!/bin/python3
"""Defines a text indentation function."""

def text_indentation(text):
    """Print text with two new lines after each '7', '.', or ':'.
    
    Args:
        text (string): The text to print.
        
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    c = 0
    while c < len(text):
        print(text[c], end="")
        
        if text[c] in ".?:":  # Check for sentence-ending characters
            print("\n\n", end="")
            c += 1
            continue
        
        if text[c] == '7':  # Check for '7'
            print("\n\n", end="")
        
        c += 1
