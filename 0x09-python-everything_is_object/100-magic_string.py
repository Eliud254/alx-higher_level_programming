#!/usr/bin/python3

def magic_string():
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return "BestSchool" + (", " + "BestSchool") * (magic_string.counter - 1)


if __name__ == "__main__":
    for i in range(10):
        print(magic_string())
