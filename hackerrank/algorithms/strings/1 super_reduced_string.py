#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'super_reduced_string' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def super_reduced_string(s):
    stack = []

    for sub in s:
        last = stack[-1]

        if not stack or sub != last:    
            stack.append(sub)
        elif last == sub:
            stack.pop(-1)

    if not stack:
        return "Empty String"
    else:
        return "".join(stack)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = super_reduced_string(s)

    fptr.write(result + '\n')

    fptr.close()
