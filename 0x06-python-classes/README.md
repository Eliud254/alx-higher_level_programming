# 0x06. Python - Classes and Objects

## Project Description
This project is focused on Object-Oriented Programming (OOP) in Python. You will be working on creating a class named Square with various attributes and methods to gain a better understanding of OOP principles in Python.

**Project started:** October 24, 2023 6:00 AM  
**Project deadline:** October 25, 2023 6:00 AM  
**Checker released:** October 24, 2023 12:00 PM  
**Auto-review:** An auto review will be launched at the deadline.

## Background Context
Object-Oriented Programming (OOP) is an essential concept in Python and programming in general. This project is designed to help you grasp the fundamentals of OOP, including understanding classes, objects, attributes, methods, and the use of properties and getters and setters.

It's important to read the provided resources in order and make sure to experiment with OOP concepts on your own. Understanding the principles of OOP will be crucial for your future projects.

## Resources
Read or watch the following materials in the order presented:

- [Object Oriented Programming](https://docs.python.org/3/tutorial/classes.html) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, classmethod and staticmethod yet).
- [Object-Oriented Programming](https://python.swaroopch.com/oop.html) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”).
- [Properties vs. Getters and Setters](https://www.python-course.eu/python3_properties.php)
- [Learn to Program 9: Object Oriented Programming](https://www.youtube.com/watch?v=jOnxYT8XmpQ)
- [Python Classes and Objects](https://www.programiz.com/python-programming/class)

## Learning Objectives
By the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What is OOP
- "first-class everything"
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected, and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the `getattr` function

## Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)

## Tasks
1. My first square
   - Write an empty class `Square` that defines a square.
   - You are not allowed to import any module.

2. Square with size
   - Write a class `Square` that defines a square with the following attributes:
     - Private instance attribute: `size`
     - Instantiation with size (no type/value verification)
   - You are not allowed to import any module.

3. Size validation
   - Write a class `Square` that defines a square with the following attributes:
     - Private instance attribute: `size`
     - Instantiation with optional size: `def __init__(self, size=0):`
     - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
     - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
   - You are not allowed to import any module.

4. Area of a square
   - Write a class `Square` that defines a square with the following attributes:
     - Private instance attribute: `size`
     - Instantiation with optional size: `def __init__(self, size=0):`
     - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
     - If `size` is less than 0, raise a `ValueError` exception with the message `size must be >= 0`
     - Public instance method: `def area(self):` that returns the current square area
   - You are not allowed to import any module.

5. Access and update private attribute
   - Write a class `Square` that defines a square with the following attributes:
     - Private instance attribute: `size`
     - Property `def size(self):` to retrieve it
     - Property setter `def size(self, value):` to set it
     - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
     - If `size` is less than 0, raise a `ValueError` exception with
