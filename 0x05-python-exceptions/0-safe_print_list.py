def safe_print_list(my_list=[], x=0):
    num = 0

    for i in range(x):
        try:
            if i >= len(my_list):
                break  # Stop if we've reached the end of the list
            print(my_list[i], end="")
            num += 1
        except IndexError:
            break

    print()
    return num
