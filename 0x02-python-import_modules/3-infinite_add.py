#!/usr/bin/python3
import sys

if len(sys.argv) < 3:
    sys.exit(1)

try:
    numbers = [int(arg) for arg in sys.argv[1:]]
except ValueError:
    sys.exit(1)

print(sum(numbers))
