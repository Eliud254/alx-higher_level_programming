#!usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            value1 = my_list_1[i] if i < len(my_list_1) else 0
            value2 = my_list_2[i] if i < len(my_list_2) else 0
            division = value1 / value2
            if isinstance(division, (int, float)):
                result.append(division)
            else:
                print("wrong type")
                result.append(0)
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)

    return result
