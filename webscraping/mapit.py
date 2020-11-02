#! python3

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
url = 'https://www.google.co.in/maps/search/' + address + '/'
webbrowser.open(url)
