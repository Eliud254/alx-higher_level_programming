def safe_print_list(my_list=[], x=0):
    num = 0

    for item in my_list:
        if num >= x:
            break

        try:
            print(item, end="")
            num += 1
        except IndexError:
            break

    print()
    return num
