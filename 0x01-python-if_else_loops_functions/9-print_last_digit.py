#!/usr/bin/python3
def print_last_digit(number):
    # Handle negative numbers correctly by using absolute value
    last_digit = abs(number % 10)
    print(last_digit)
