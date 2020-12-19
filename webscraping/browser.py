import webbrowser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('text', help="text to be searched with google'")

args = parser.parse_args()

url = "https://www.google.com/search?q=" + args.text
webbrowser.open(url)
