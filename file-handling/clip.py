# this program let you copy a file text from path
import pyperclip as pc
import argparse
import os

parser = argparse.ArgumentParser(description="Copy text from a file")
parser.add_argument("filename", help="filename which text to be copied")
args = parser.parse_args()
cwd = os.getcwd()

filepath = cwd + "/" + args.filename

with open(filepath, 'r') as f:
    text = f.read()
    pc.copy(text)


