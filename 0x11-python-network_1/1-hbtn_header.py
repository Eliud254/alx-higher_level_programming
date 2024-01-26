#!/usr/bin/python3
"""
To displays the value of the X-Request-Id variable
found in a header of the response
"""
import urllib.request
from sys import argv


def main(argv):
    """
    Ways on how  to takes in the URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response
    """
    url = argv
    with urllib.request.urlopen(url) as response:
        headers = response.info()
        print(headers['X-Request-Id'])


if __name__ == "__main__":
    main(argv[1])
