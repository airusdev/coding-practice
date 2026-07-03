#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# solution here
def diagonalDifference(arr):
    left_diagonal = 0
    right_diagonal = 0

    for i in range(0,len(arr)):
        left_diagonal += arr[i][i]
        right_diagonal += arr[i][len(arr) - i - 1]    

    total = abs(left_diagonal - right_diagonal)
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
