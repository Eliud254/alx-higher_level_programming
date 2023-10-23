def safe_print_list(my_list=[], x=0):
    printed_count = 0

    for i in range(x):
        try:
            print(my_list[i], end='')
            printed_count += 1
        except IndexError:
            break  # Exit the loop if the index is out of range

    print()  # Add a new line at the end
    return printed_count
