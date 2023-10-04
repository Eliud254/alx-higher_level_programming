# Project Title: Python Hello World

## Table of Contents

- [Description](#description)
- [Concepts](#concepts)
- [Author's Disclaimer](#authors-disclaimer)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Run Python file](#task-0-run-python-file)
  - [Task 1: Run inline](#task-1-run-inline)
  - [Task 2: Hello, print](#task-2-hello-print)
  - [Task 3: Print integer](#task-3-print-integer)
  - [Task 4: Print float](#task-4-print-float)
  - [Task 5: Print string](#task-5-print-string)
  - [Task 6: Play with strings](#task-6-play-with-strings)
  - [Task 7: Copy - Cut - Paste](#task-7-copy-cut-paste)
  - [Task 8: Create a new sentence](#task-8-create-a-new-sentence)
  - [Task 9: Easter Egg](#task-9-easter-egg)
  - [Task 10: Linked list cycle](#task-10-linked-list-cycle)

## Description

Welcome to the Python world! This project introduces you to Python programming through a series of tasks. Python is known for its simplicity and readability, and you'll get to explore various aspects of the language.

## Concepts

For this project, you will focus on the following concept:

- Python programming

## Author's Disclaimer

The initial projects in Python are designed to be simple and "C-oriented," with straightforward tasks and no complex or tricky syntax. As you progress, you'll discover the flexibility of Python and its multiple ways of accomplishing tasks. Be prepared for a journey that will gradually introduce more fun and challenging aspects of Python.

## Resources

To complete this project, you'll need to refer to the following resources:

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) (Read the first three chapters)
  - Whetting Your Appetite
  - Using the Python Interpreter
  - An Informal Introduction to Python (Read up until "3.1.2. Strings" included)
- [How To Use String Formatters in Python 3](https://docs.python.org/3/library/string.html#formatstrings)
- [PEP8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Learning Objectives

Upon completing this project, you should be able to:

- Explain why Python programming is awesome.
- Describe who created Python.
- Identify Guido van Rossum as the creator of Python.
- Explain the origin of the name "Python."
- Define the Zen of Python.
- Use the Python interpreter.
- Print text and variables using the `print` function.
- Work with strings.
- Understand indexing and slicing in Python.
- Follow the official Python coding style (PEP8) and check your code with `pycodestyle`.

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your Python files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your Python files should end with a new line.
- The first line of all your Python files should be exactly `#!/usr/bin/python3`.
- You must include a `README.md` file at the root of the repository, describing the repository.
- A `README.md` file must be present at the root of the project directory.
- Your Python code should use `pycodestyle` (version 2.8.*).
- All your Python files must be executable.
- The length of your Python files will be tested using `wc`.

### Shell Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your shell scripts will be tested on Ubuntu 20.04 LTS.
- All your shell scripts should be exactly two lines long (use `wc -l` to check).
- All your shell scripts should end with a new line.
- The first line of all your shell scripts should be exactly `#!/bin/bash`.
- All your shell scripts must be executable.

### C Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your C files will be compiled on Ubuntu 20.04 LTS using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`.
- All your C files should end with a new line.
- Your C code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`.
- You are not allowed to use global variables.
- No more than 5 functions per file.
- The prototypes of all your functions should be included in your header file called `lists.h`.
- Don't forget to push your header file.
- All your header files should be include guarded.

## Tasks

### Task 0: Run Python file

Write a Shell script that runs a Python script.

- The Python file name will be saved in the environment variable `$PYFILE`.

#### Example:

```bash
$ cat main.py
#!/usr/bin/python3
print("Best School")

$ export PYFILE=main.py
$ ./0-run
Best School
```

### Task 1: Run inline

Write a Shell script that runs Python code.

- The Python code will be saved in the environment variable `$PYCODE`.

#### Example:

```bash
$ export PYCODE='print(f"Best School: {88+10}")'
$ ./1-run_inline
Best School: 98
```

### Task 2: Hello, print

Write a Python script that prints exactly "Programming is like building a multilingual puzzle," followed by a new line.

- Use the `print` function.

#### Example:

```bash
$ ./2-print.py
"Programming is like building a multilingual puzzle
```

### Task 3: Print integer

Complete the provided source code to print the integer stored in the variable `number`, followed by "Battery street," followed by a new line.

- You cannot cast the variable `number` into a string.
- Your code must be 3 lines long.
- You must use f-strings.

#### Example:

```bash
$ ./3-print_number.py
98 Battery street
```

### Task 4: Print float

Complete the provided source code to print the float stored in the variable `number` with a precision of 2 digits.

- You cannot cast the variable `number` to a string.
- You must use f-strings.

#### Example:

```bash
$ ./4-print_float.py
Float: 3.14
```

### Task 5: Print string

Complete the provided source code to print the string stored in the variable `str` three times, followed by its first 9 characters.

- You cannot use any loops or conditional statements.
- Your program should be a maximum of 5 lines long.

#### Example:

```bash
$ ./5-print_string.py
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

### Task 6

: Play with strings

Complete the provided source code to print "Welcome to Holberton School!"

- You cannot use any loops or conditional statements.
- You must use the variables `str1` and `str2` in your new line of code.
- Your program should be exactly 5 lines long.

#### Example:

```bash
$ ./6-concat.py
Welcome to Holberton School!
```

### Task 7: Copy - Cut - Paste

Complete the provided source code to display the following:

- The first 3 letters of the variable `word` as "First 3 letters: `str1`"
- The last 2 letters of the variable `word` as "Last 2 letters: `str2`"
- The value of the variable `word` without the first and last letters as "Middle word: `str3`"

- You cannot use any loops or conditional statements.
- Your program should be exactly 8 lines long.

#### Example:

```bash
$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

### Task 8: Create a new sentence

Complete the provided source code to print "object-oriented programming with Python," followed by a new line.

- You cannot use any loops or conditional statements.
- Your program should be exactly 5 lines long.
- You cannot create new variables.
- You cannot use string literals.

#### Example:

```bash
$ ./8-concat_edges.py
object-oriented programming with Python
```

### Task 9: Easter Egg

Write a Python script that prints "The Zen of Python," by Tim Peters, followed by a new line.

- Your script should be a maximum of 98 characters long (please check with `wc -m`).

#### Example:

```bash
$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
Let's do more of those!
```

### Task 10: Linked list cycle

Write a function in C that checks if a singly linked list has a cycle in it.

- Prototype: `int check_cycle(listint_t *list);`
- Return: `0` if there is no cycle, `1` if there is a cycle.
- Requirements:
  - You can only use the following functions: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`.
- You are not allowed to use global variables.
- No more than 5 functions per file.
- The prototypes of all your functions should be included in your header file called `lists.h`.
- Don't forget to push your header file.
- All your header files should be include guarded.

#### Example:

```bash
$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
$ ./cycle
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
```

Solving a problem is already a big win, but finding the best and optimal way to solve it is even better! Consider the most optimal and efficient approach to each task.
