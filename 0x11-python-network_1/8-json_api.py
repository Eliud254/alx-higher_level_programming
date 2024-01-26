#!/usr/bin/python3
"""
Send  POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv


def main(argv):
    """
     Takes in the letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as the parameter.
    """
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    payload = {'q': q}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data=payload)
    try:
        result = r.json()
        if bool(result) is False:
            print("No result")
        else:
            print("[{}] {}".format(result['id'], result['name']))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main(argv)
