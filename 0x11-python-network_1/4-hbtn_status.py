#!/usr/bin/python3
"""
Using module request that fetches https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    """
    A function that fetches https://alx-intranet.hbtn.io/status
    """
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))


if __name__ == "__main__":
    main()
