#!usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            value1 = my_list_1[i] if i < len(my_list_1) else 0
            value2 = my_list_2[i] if i < len(my_list_2) else 0

            if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
                if value2 == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(value1 / value2)
            else:
                result.append(0)
                print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")

    return result
