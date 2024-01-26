#!/usr/bin/python3
"""
Request POST to the passed URL with the email as the parameter
"""
import requests
from sys import argv


def main(argv):
    """
    POST request to  passed URL with the email as the parameter,
    and displays the body of the response.
    """
    values = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, data=values)
    print(r.text)


if __name__ == "__main__":
    main(argv)
