#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    # Argument assignment and conversion
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Map operator to the corresponding function
    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    # Validate operator
    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Perform calculation and output result
    result = operations[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
