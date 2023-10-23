def safe_print_list(my_list=[], x=0):
    printed_count = 0

    try:
        for i in range(x):
            print(my_list[i], end='')
            printed_count += 1
    except IndexError:
        pass

    print()
    return printed_count
