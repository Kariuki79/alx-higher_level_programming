#!/usr/bin/python3

# This program prints the lowercase ASCII alphabet without a newline.
# It adheres to the constraints:
# - Uses only one print function with string format.
# - Uses only one loop.
# - Does not store characters in a variable explicitly.
# - Does not import any module.
print("{}".format("".join(chr(97 + i) for i in range(26))), end="")
