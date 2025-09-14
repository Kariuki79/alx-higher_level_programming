#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # sys.argv[1:] → List of all arguments except the script name
    args = sys.argv[1:]

    # Convert each argument to int and sum them
    total = sum(int(arg) for arg in args)

    # Print the result followed by a newline
    print(total)
