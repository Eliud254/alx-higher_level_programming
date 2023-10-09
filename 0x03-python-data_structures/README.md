# Readme File for Python - Data Structures: Lists, Tuples (Project 0x03)

## Introduction

This project focuses on Python's data structures, specifically lists and tuples. It covers a range of tasks related to these data structures to help you understand their usage, differences, and common methods. The project also includes a CPython task that explores the inner workings of Python lists.

## Project Details

- **Author:** Guillaume
- **Project Start Date:** October 6, 2023, 6:00 AM
- **Project End Date:** October 10, 2023, 6:00 AM
- **Checker Release Date:** October 7, 2023, 6:00 AM
- **Auto Review:** An auto review will be launched at the deadline

## Learning Objectives

By completing this project, you will gain knowledge and skills in the following areas:

### General
- Understanding why Python programming is awesome
- Working with lists and knowing how to use them
- Recognizing the differences and similarities between strings and lists
- Mastering common list methods and their usage
- Using lists as stacks and queues
- Understanding list comprehensions and applying them
- Getting familiar with tuples and their usage
- Knowing when to use tuples versus lists
- Understanding what a sequence is
- Exploring tuple packing and sequence unpacking
- Learning about the `del` statement and how to use it

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use the `pycodestyle` (version 2.8.*) coding style
- All your files must be executable
- The length of your files will be tested using `wc`

### C

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All your files should end with a new line
- Your code should use the Betty style, which will be checked using `betty-style.pl` and `betty-doc.pl`
- You are not allowed to use global variables
- No more than 5 functions per file
- Prototypes of all your functions should be included in your header file called `lists.h`
- Don't forget to push your header file
- All your header files should be include guarded

## Project Tasks

1. **Print a list of integers**
   - Write a function that prints all integers of a list.
   - Prototype: `def print_list_integer(my_list=[])`
   - Format: one integer per line.
   - You are not allowed to import any module.
   - You can assume that the list only contains integers.
   - You are not allowed to cast integers into strings.
   - You have to use `str.format()` to print integers.

2. **Secure access to an element in a list**
   - Write a function that retrieves an element from a list like in C.
   - Prototype: `def element_at(my_list, idx)`
   - If idx is negative, the function should return None.
   - If idx is out of range (> number of elements in my_list), the function should return None.
   - You are not allowed to import any module.
   - You are not allowed to use try/except.

3. **Replace element**
   - Write a function that replaces an element of a list at a specific position (like in C).
   - Prototype: `def replace_in_list(my_list, idx, element)`
   - If idx is negative, the function should not modify anything and should return the original list.
   - If idx is out of range (> number of elements in my_list), the function should not modify anything and should return the original list.
   - You are not allowed to import any module.
   - You are not allowed to use try/except.

4. **Print a list of integers... in reverse!**
   - Write a function that prints all integers of a list in reverse order.
   - Prototype: `def print_reversed_list_integer(my_list=[])`
   - Format: one integer per line.
   - You are not allowed to import any module.
   - You can assume that the list only contains integers.
   - You are not allowed to cast integers into strings.
   - You have to use `str.format()` to print integers.

5. **Replace in a copy**
   - Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
   - Prototype: `def new_in_list(my_list, idx, element)`
   - If idx is negative, the function should return a copy of the original list.
   - If idx is out of range (> number of elements in my_list), the function should return a copy of the original list.
   - You are not allowed to import any module.
   - You are not allowed to use try/except.

6. **Lists of lists = Matrix**
   - Write a function that prints a matrix of integers.
   - Prototype: `def print_matrix_integer(matrix=[[]])`
   - Format: see example.
   - You are not allowed to import any module.
   - You can assume that the list only contains integers.
   - You are not allowed to cast integers into strings.
   - You have to use `str.format()` to print integers.

7. **Tuples addition**
   - Write a function that adds 2 tuples.
   - Prototype: `def add_tuple(tuple_a=(), tuple_b=())`
   - Returns a tuple with 2 integers:
     - The first element should be the addition of the first element of each argument.
     - The second element should be the addition of the second element of each argument.
   - You are not allowed to import any module.
   - You can assume that the two tuples will only contain integers.
   - If a tuple is smaller than 2, use the value 0 for each missing integer.
   - If a tuple is bigger than 2, use only the first 2 integers.

8. **More returns!**
   - Write a function that returns a tuple with the length of a string and its first character.
   - Prototype: `def multiple_returns(sentence)`
   - If the sentence is empty, the first character should be equal to None.
   - You are not allowed to import any module.

9. **Find the max**
   - Write a function that finds the biggest integer in a list.
   - Prototype: `def max_integer(my_list=[])`
   - If the list is empty, return None.
   - You can assume that the list only contains integers.
   - You are not allowed to import any module.
   - You are not allowed to use the built-in `max()` function.

10. **Only by 2**
    - Write a function that finds all multiples of 2 in a list.
    - Prototype: `def divisible_by_2(my_list=[])`
    - Return a new list with True or False,

 depending on whether the integer at the same position in the original list is a multiple of 2.
    - The new list should have the same size as the original list.
    - You are not allowed to import any module.

11. **Delete at**
    - Write a function that deletes the item at a specific position in a list.
    - Prototype: `def delete_at(my_list=[], idx=0)`
    - If idx is negative or out of range, nothing changes (returns the same list).
    - You are not allowed to use `pop()`.
    - You are not allowed to import any module.

12. **Switch (Advanced)**
    - Complete the source code to switch the values of `a` and `b`.
    - Your code should be inserted where the comment is (line 4).
    - Your program should be exactly 5 lines long.

13. **Linked list palindrome (Advanced)**
    - Write a function in C that checks if a singly linked list is a palindrome.
    - Prototype: `int is_palindrome(listint_t **head);`
    - Return 0 if it is not a palindrome, 1 if it is a palindrome.
    - An empty list is considered a palindrome.

14. **CPython #0: Python lists (Advanced)**
    - Create a C function that prints basic info about Python lists.
    - Prototype: `void print_python_list_info(PyObject *p);`
    - Python version: 3.4
    - Your shared library will be compiled with the specified command line.
    - The Python version used for this task is 3.4.
    - OS: Ubuntu 14.04 LTS.

## Getting Started

To get started with this project, you can follow these steps:

1. Clone the GitHub repository: [alx-higher_level_programming](https://github.com/your_username/alx-higher_level_programming).

2. Navigate to the directory of the project: `0x03-python-data_structures`.

3. Inside this directory, you will find the Python and C files for each task.

4. You can use the provided `*.py` files for Python tasks and the `*.c` files for C tasks.

5. Implement your solutions in these files as per the task requirements.

6. Remember to create a `README.md` file at the root of the project folder to document your work and provide explanations for each task.

## Testing

You can test your Python scripts by running them in your preferred Python environment (Python 3.8.5) or by using the provided test files (e.g., `0-main.py`, `1-main.py`, etc.) with sample inputs.

For the C tasks, you can compile the C files and execute the resulting binary to test your code. Use the provided test scripts and sample inputs to verify the correctness of your C functions.

## Conclusion

This project will help you solidify your understanding of Python's data structures, specifically lists and tuples. It also includes some C tasks to explore the inner workings of Python and CPython. Complete the tasks and ensure your code meets the specified requirements to successfully complete this project. Good luck!
