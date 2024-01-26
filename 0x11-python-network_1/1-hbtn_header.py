#!/usr/bin/python3
"""
To displays the value of the X-Request-Id variable
"""
import urllib.request
from sys import argv


def main(argv):

    url = argv
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers['X-Request-Id'])


if __name__ == "__main__":
    main(argv[1])
