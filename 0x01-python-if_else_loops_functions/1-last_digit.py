#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = number % 10

# Adjust last_digit for negative numbers to match negative example output
if number < 0 and last_digit != 0:
    last_digit = - (abs(number) % 10)

output_string = f"last digit of {number} is {last_digit}"
if last_digit > 5:
    output_string += " and is greater than 5"
elif last_digit == 0:
    output_string += " and is 0"
elif last_digit < 6  and last_digit != 0:
    output_string += " and is less than 6 and not 0"

print(output_string)
