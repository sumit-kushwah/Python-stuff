import os
import argparse

parser = argparse.ArgumentParser(description="rename extension")
parser.add_argument('olde', metavar="old-extension")
parser.add_argument('newe', metavar="new-extension")

validextensions = ['cpp', 'c', 'py', 'php', 'html', 'cc', 'htm', 'js', 'ts', 'txt']

args = parser.parse_args()
olde = args.olde
newe = args.newe

if (olde in validextensions and newe in validextensions):
    files = os.listdir()
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension == ('.' + olde):
            os.rename(file, filename + '.' + newe)
    
else:
    print("One of extension is not in following list.")
    print(validextensions)
