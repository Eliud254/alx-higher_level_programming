# Project Title: 0x04. Python - More Data Structures: Set, Dictionary

## Introduction

This project is part of the "0x04. Python - More Data Structures: Set, Dictionary" project series at ALX - Holberton School. The goal of this project is to learn more about Python programming and explore the concepts of sets and dictionaries, as well as related functions and operations.

## Learning Objectives

By the end of this project, you will be able to:

- Explain why Python programming is awesome.
- Understand the concept of sets and how to use them.
- Know the most common methods of sets and how to use them.
- Learn when to use sets versus lists.
- Iterate into a set and perform operations.
- Understand dictionaries and how to use them.
- Know when to use dictionaries versus lists or sets.
- Define what a key in a dictionary is.
- Learn how to iterate over a dictionary.
- Understand what a lambda function is.
- Know the use of the map, reduce, and filter functions.

## Requirements

- Allowed editors: vi, vim, emacs.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
- All your files should end with a newline.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should adhere to the PEP 8 style guide (use pycodestyle version 2.8.*).
- All your files must be executable.
- The length of your files will be tested using the `wc` command.

## Tasks

### 0. Squared Simple

Write a function that computes the square value of all integers of a matrix.

- Prototype: `def square_matrix_simple(matrix=[]):`
- `matrix` is a 2-dimensional array.
- Returns a new matrix (of the same size as `matrix`).
- Each value should be the square of the value of the input.
- The initial matrix should not be modified.
- You are not allowed to import any modules.
- You are allowed to use regular loops, map, etc.

Example:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
```

Output:

```
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### 1. Search and Replace

Write a function that replaces all occurrences of an element by another in a new list.

- Prototype: `def search_replace(my_list, search, replace):`
- `my_list` is the initial list.
- `search` is the element to replace in the list.
- `replace` is the new element.
- You are not allowed to import any modules.

Example:

```python
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)
print(new_list)
print(my_list)
```

Output:

```
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```

### 2. Unique Addition

Write a function that adds all unique integers in a list (only once for each integer).

- Prototype: `def uniq_add(my_list=[]):`
- You are not allowed to import any modules.

Example:

```python
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
```

Output:

```
Result: 15
```

### 3. Present in Both

Write a function that returns a set of common elements in two sets.

- Prototype: `def common_elements(set_1, set_2):`
- You are not allowed to import any modules.

Example:

```python
set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))
```

Output:

```
['C']
```

### 4. Only Differents

Write a function that returns a set of all elements present in only one set.

- Prototype: `def only_diff_elements(set_1, set_2):`
- You are not allowed to import any modules.

Example:

```python
set_1 = {"Python", "C", "Javascript"}
set_2 = {"Bash", "C", "Ruby", "Perl"}
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
```

Output:

```
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```

### 5. Number of Keys

Write a function that returns the number of keys in a dictionary.

- Prototype: `def number_keys(a_dictionary):`
- You are not allowed to import any modules.

Example:

```python
a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))
```

Output:

```
Number of keys: 3
```

### 6. Print Sorted Dictionary

Write a function that prints a dictionary by ordered keys.

- Prototype: `def print_sorted_dictionary(a_dictionary):`
- You can assume that all keys are strings.
- Keys should be sorted by alphabetic order.
- Only sort keys of the first level (don't sort keys of a dictionary inside the main dictionary).
- Dictionary values can have any type.
- You are not allowed to import any modules.

Example:

```python
a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
print_sorted_dictionary(a_dictionary)
```

Output:

```
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```

### 7. Update Dictionary

Write a function that replaces or adds key/value in a dictionary.

- Prototype: `def update_dictionary(a_dictionary, key, value):`
- `key` argument will always be a string.
- `value` argument will be of any type.
- If a key exists in the dictionary, the value will be replaced.
- If a key doesn't exist in the dictionary, it will be created.
- You are not allowed to import any modules.

Example:

```python
a_dictionary = {'language': "C", 'number':

 89, 'track': "Low level"}
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
print("--")
print("--")
new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
```

Output:

```
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
```

### 8. Simple Delete by Key

Write a function that deletes a key in a dictionary.

- Prototype: `def simple_delete(a_dictionary, key=""):`
- `key` argument will always be a string.
- If a key doesn't exist, the dictionary won't change.
- You are not allowed to import any modules.

Example:

```python
a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
```

Output:

```
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
```

### 9. Multiply by 2

Write a function that returns a new dictionary with all values multiplied by 2.

- Prototype: `def multiply_by_2(a_dictionary):`
- You can assume that all values are only integers.
- Returns a new dictionary.
- You are not allowed to import any modules.

Example:

```python
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
```

Output:

```
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
```

### 10. Best Score

Write a function that returns a key with the biggest integer value.

- Prototype: `def best_score(a_dictionary):`
- You can assume that all values are only integers.
- If no score is found, return `None`.
- You can assume all students have a different score.
- You are not allowed to import any modules.

Example:

```python
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
```

Output:

```
Best score: Molly
Best score: None
```

### 11. Multiply by Using Map

Write a function that returns a list with all values multiplied by a number without using any loops.

- Prototype: `def multiply_list_map(my_list=[], number=0):`
- Returns a new list (of the same length as `my_list`).
- Each value should be multiplied by `number`.
- The initial list should not be modified.
- You are not allowed to import any modules.
- You have to use `map`.

Example:

```python
my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)
```

Output:

```
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
```

### 12. Roman to Integer

Create a function `def roman_to_int(roman_string):` that converts a Roman numeral to an integer.

- You can assume the number will be between 1 to 3999.
- `roman_to_int(roman_string)` must return an integer.
- If the `roman_string` is not a string or `None`, return `0`.

Example:

```python
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
```

Output:

```
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
```

## Summary

This project delves into advanced Python data structures, including sets and dictionaries, and provides an opportunity to practice various data manipulation tasks. By completing these tasks, you'll enhance your understanding of Python's capabilities and become more proficient in working with data structures.
