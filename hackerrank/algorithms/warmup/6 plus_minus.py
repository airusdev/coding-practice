#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# my solution
def plusMinus(arr):
    positives = 0.0
    negatives = 0.0
    zeroes = 0.0

    for num in arr:
        if num > 0:
            positives += 1
        elif num < 0:
            negatives += 1
        else:
            zeroes += 1
    
    print(f"{(positives / len(arr)):.6f}")
    print(f"{(negatives / len(arr)):.6f}")
    print(f"{(zeroes / len(arr)):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
