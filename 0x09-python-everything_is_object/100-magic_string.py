#!/usr/bin/python3

def magic_string():
    magic_string.word_list = getattr(magic_string, 'word_list', []) + ["Holberton"]
    return ", ".join(magic_string.word_list)

if __name__ == "__main__":
    for i in range(10):
        print(magic_string())
