#!/usr/bin/pyhon3
def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0  # Initialize a counter for the printed integers

    for i in range(x):
        try:
            # Try to convert the current element to an integer and print it
            # If it's an integer, print it; if not, it will raise a ValueError
            element = my_list[i]
            if isinstance(element, int):
                print("{:d}".format(element), end="")
                printed_integers += 1
        except (ValueError, TypeError, IndexError):
            # Handle exceptions:
            # - ValueError: when the element cannot be converted to an integer
            # - TypeError: if isinstance check fails (e.g., for strings)
            # - IndexError: when the list is exhausted before printing 'x' integers
            pass

    print()
    return printed_integers
