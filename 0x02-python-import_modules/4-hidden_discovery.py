#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    # Get every attribute/function name from the module
    names = dir(hidden_4)

    # Print those that do not start with "__", in alphabetical order
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
