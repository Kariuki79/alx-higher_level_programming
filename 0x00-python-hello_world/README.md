cat << 'EOF' > README.md
# 0x00. Python - Hello, World

## Description
This project marks the transition from C low-level programming to Python 3 in the ALX Software Engineering curriculum. It covers the core foundational concepts of Python: running scripts and inline code with the interpreter, standard output formatting, string manipulation (indexing, slicing, concatenation, repetition), adhering strictly to PEP 8 standards via `pycodestyle`, and inspecting Python bytecode. It also includes an algorithmic C challenge testing singly linked list cycle detection.

---

## Learning Objectives
By the end of this project, you are expected to be able to explain:
- Why Python programming is awesome
- Who created Python and why "Python" was chosen
- The philosophy of the Zen of Python
- How to use the Python interactive shell and run scripts
- How to print strings and format variables using `print`
- How strings work: indexing, slicing, immutability, and concatenation
- The official Python coding style (PEP 8) and how to validate code with `pycodestyle`

---

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files must end with a new line
- The first line of all your files must be exactly `#!/usr/bin/python3`
- Code must use the `pycodestyle` style guide (version 2.8.*)
- All files must be executable (`chmod u+x`)
- The length of your files will be tested using `wc`

### Shell Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- Executed on Ubuntu 20.04 LTS
- All scripts must be two lines long (`wc -l` will be checked)
- All files must be executable (`chmod u+x`)
- The first line of all your files must be exactly `#!/bin/bash`

### C Files
- Allowed editors: `vi`, `vim`, `emacs`
- Compiled with `gcc 9.4.0` using the flags `-Wall -Werror -Wextra -pedantic -std=gnu89`
- Code must follow the Betty style guide (`betty-style.pl` and `betty-doc.pl`)
- No global variables
- No more than 5 functions per file

---

## Tasks Overview

| File | Description |
|---|---|
| `0-run` | Bash script that runs a Python script specified by the `$PYFILE` environment variable |
| `1-run_inline` | Bash script that runs Python code passed in the `$PYCODE` environment variable |
| `2-print.py` | Python script that prints `"Programming is like building a multilingual puzzle"` followed by a new line |
| `3-print_number.py` | Python script that prints an integer stored in a variable followed by `Battery street` |
| `4-print_float.py` | Python script that prints a float rounded to 2 decimal places |
| `5-print_string.py` | Python script that prints a string 3 times, followed by its first 9 characters |
| `6-concat.py` | Python script that concatenates two string variables |
| `7-edges.py` | Python script demonstrating string slicing (first 3, last 2, and middle characters) |
| `8-concat_edges.py` | Python script that extracts and prints specific sentence components using slice syntax |
| `9-easter_egg.py` | Python script that prints The Zen of Python (`import this`) within 98 characters |
| `10-check_cycle.c`, `lists.h` | C function that checks if a singly linked list contains a cycle (Floyd's Cycle-Finding Algorithm) |
| `100-write.py` | Python script that prints a string to `stderr` and exits with status code `1` using `sys` |
| `101-compile` | Bash script that compiles a Python script file into bytecode (`.pyc`) |
| `102-magic_calculation.py` | Python function decompiled from specific CPython bytecode |

---

## Author
Kariuki Mwangi
EOF
