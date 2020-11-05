import argparse
import sys

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator') 
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
# we can also pass our list of arguments to parse_args funciton
# by default it takes list from sys.argv
args = parser.parse_args() 
print(args.accumulate(args.integers))
