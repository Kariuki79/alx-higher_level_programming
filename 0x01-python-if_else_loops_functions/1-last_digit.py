#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    n = number % 10
else:
    n = -(abs(number) % 10)

print(f"Last digit of {number} is {n}", end=" ")

if n > 5:
    print(f"and is greater than 5")
elif n == 0:
    print(f"and is 0")
else:
    print(f"and is less than 6 and not 0")
