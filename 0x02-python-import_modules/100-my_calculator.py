#!/usr/bin/python3

# import an execution block
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    # Check the number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)


    # Argument Assignment and Conversion
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    # Operator Mapping
    # Map operator to the corresponding functions
    operations = {
            '+' : add,
            '-' : sub,
            '*' : mul,
            '/' : div
    }

    # Operator Validation
    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    # Calculation and Output
    result = operations[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
