# 0x02. Python - import & modules

## Table of Contents

- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)

## Description

Welcome to the 0x02. Python - import & modules project! In this project, we will explore various aspects of Python programming, including importing functions from other files, creating modules, working with command line arguments, and more.

## Learning Objectives

By the end of this project, you will be able to:

- Explain why Python programming is awesome.
- Import functions from another file.
- Use imported functions.
- Create a module.
- Use the built-in function `dir()`.
- Prevent code in your script from being executed when imported.
- Use command line arguments with your Python programs.

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use pycodestyle (version 2.8.\*) for style compliance
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

### 0. Import a simple function from a simple file

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

- You have to use the `print` function with string format to display integers.
- Assign the value `1` to a variable called `a`.
- Assign the value `2` to a variable called `b`.
- Use those two variables as arguments when calling the functions `add` and `print`.
- `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`.
- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed by a new line.
- You can only use the word `add_0` once in your code.
- You are not allowed to use `*` for importing or `__import__`.
- Your code should not be executed when imported.

**Example:**

```bash
$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

$ ./0-add.py
1 + 2 = 3
$ cat 0-import_add.py
__import__("0-add")

$ python3 0-import_add.py
$

