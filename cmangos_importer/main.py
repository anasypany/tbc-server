#!/usr/bin/python3
from string import Template
import sys
import os.path
from src.parser import parse_file
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--account", help="Account Name (defaults to Character Name when left empty)")
parser.add_argument("-e", "--expansion", help="Expansion Flag (0 for 1.13.x, 1 for 2.4.x (default when unset is 1)", default='1', type=int)
parser.add_argument("-f", "--file", help="Path to file containing character dump info", required=True)
args = parser.parse_args()

if args.account is not None:
    account_name = args.account
else:
    account_name = "notprovided"

file_path = args.file
expansion = args.expansion


# if sys.stdin and sys.stdin.isatty():
#     # check if ran from cli
#     if len(sys.argv) == 2:
#         filepath = sys.argv[1]
#     elif len(sys.argv) == 3:
#         filepath = sys.argv[1]
#         if sys.argv[2].isdecimal():
#             expansion = int(sys.argv[2])
#     elif len(sys.argv) == 1:
#         print("Usage: ./main.py path_to_the_file")
#         sys.exit(0)
#     else:
#         sys.exit(1)
# else:
#     filepath = "./exported.txt"


if os.path.isfile(file_path):
    print("file name: " + file_path + '\naccount name: ' + account_name + '\nexpansion id: ' + str(expansion))
    with open(file_path) as file:
        parse_file(file.readlines(), expansion, account_name)
