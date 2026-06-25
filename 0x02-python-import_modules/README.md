# 0x02. Python - Import & Modules

## Description
This project covers the fundamentals of modules, importing functions, and managing executable code scopes in Python 3. It explores how to structure clean codebases, pass command-line arguments using `sys.argv`, and safely utilize built-in functions like `dir()`.

## Learning Objectives
By the end of this project, I learned:
* How to import functions from other files/modules.
* How to use the built-in function `dir()`.
* How to prevent code from executing when imported using `if __name__ == "__main__":`.
* How to handle command-line arguments dynamically using `sys.argv`.

## Requirements
* All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
* Code adheres to the `pycodestyle` (version 2.8.*) style guide.
* All source files must be executable (`chmod u+x filename.py`).

## File Directory & Tasks

| File | Description |
| --- | --- |
| `0-add.py` | Imports an addition function from a separate file and displays the calculated output format. |
| `1-calculation.py` | Imports multiple mathematical functions from a single file to execute basic arithmetic equations. |
| `2-args.py` | Prints the exact count and list of all parameters passed into it via the command line. |
| `3-infinite_add.py` | Collects all numerical command-line arguments and calculates their cumulative sum. |
| `4-hidden_discovery.py` | Imports a compiled `.pyc` module, extracts all internal attributes using `dir()`, filters out dunder methods, and prints them in. |
| `5-variable_load.py` | Imports a specific global variable (`a`) from an external module and prints its stored value. |
