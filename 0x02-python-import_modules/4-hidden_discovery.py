#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Fetch all names inside the module
    all_names = dir(hidden_4)

    # Sort names alphabetically and print if they don't start with '__'
    for name in sorted(all_names):
        if not name.startswith("__"):
            print("{}".format(name))
