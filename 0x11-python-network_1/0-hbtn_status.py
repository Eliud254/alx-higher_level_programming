#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.reguest

def main()
"""
The function to print the reponse of the specific url
"""
url = 'https://alx-intranet.hbtn.io/statu'
with urllib.request.urlopen(url) as response:
    htm = response.read()
    print('body response:')
    print('Body response:')
    print('\t- content: {}'.format(html))
    print('\t- utf8 content: {}'.format(html.decode('utf8')))

    if _name_ == "_main_":
        main()
