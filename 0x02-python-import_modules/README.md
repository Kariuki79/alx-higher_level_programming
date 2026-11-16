# 0x02. Python - import & modules

## Description
This project covers importing functions from external Python modules, controlling top-level script execution with `__name__ == "__main__"`, parsing command-line arguments via `sys.argv`, and inspecting module namespaces using `dir()`.

## Requirements
* Operating System: Ubuntu 20.04 LTS
* Python Version: Python 3.8.5
* Style Guide: `pycodestyle` (version 2.8.*)
* All files are executable and end with a newline.
* The first line of all Python scripts is `#!/usr/bin/python3`.

## File Index
| File | Description |
|---|---|
| `0-add.py` | Imports `add` from `add_0` and prints the result of `1 + 2 = 3` |
| `1-calculation.py` | Imports `add`, `sub`, `mul`, and `div` from `calculator_1` and prints results |
| `README.md` | Project documentation and file index |
| `2-args.py` | Prints the number of command-line arguments passed and lists each one. |
| `3-infinite_add.py` | Prints the sum of all integer arguments passed via the command line. |
| `4-hidden_discovery.py` | Prints all public names defined inside the compiled module `hidden_4.pyc`. |
| `5-variable_load.py` | Imports the variable `a` from `variable_load_5.py` and prints its value. |
| `100-my_calculator.py` | Handles basic arithmetic operations (`+`, `-`, `*`, `/`) passed as CLI arguments. |
| `101-easy_print.py` | Prints `#pythoniscool` without using `print`, `eval`, `open`, or `sys`. |
| `102-magic_calculation.py` | Replicates the behavior of a provided Python bytecode function. |
| `103-fast_alphabet.py` | Prints the uppercase alphabet without loops, conditionals, or string literals. |
