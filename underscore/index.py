#!/usr/bin/env python3 

import sys

def simple_print(str):
    print('Simple printing: ' + str)

if __name__ == "__main__":
    arg = sys.argv
    print(arg)

    [first, str] = sys.argv[2:4]

    if sys.argv[1] == 'simple_print':
        simple_print(str)
