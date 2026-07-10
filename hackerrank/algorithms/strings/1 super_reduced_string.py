#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def super_reduced_string(s):
    stack = set()
    
    for letter in s:
        if letter not in stack:
            stack.add(letter)
        else:
            stack.remove(letter)
            continue
    
    return "".join(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = super_reduced_string(s)

    fptr.write(result + '\n')

    fptr.close()
