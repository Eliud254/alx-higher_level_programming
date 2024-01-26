#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


def main():
    """
    A funtion to print a response of a specific url
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))


if __name__ == "__main__":
    main()
