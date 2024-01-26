#!/usr/bin/python3
"""
Request to an URL and displays the body of the response.
"""
import requests
from sys import argv


def main(argv):
    """
    How to manage urllib.error.HTTPError exceptions and
    print: Error code: followed by the HTTP status code
    """
    url = argv[1]
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))


if __name__ == "__main__":
    main(argv)
