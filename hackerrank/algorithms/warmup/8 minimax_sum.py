#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minimum = min(arr)
    maximum = max(arr)

    min_sum = 0
    max_sum = 0

    for num in arr:
       if num != minimum:
           max_sum += num
       if num != maximum:
           min_sum += num 

    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


"""
get minimum
get maximum

first loop: add to min_sum if not maximum
second loop: add to max_sum if not minimum

input: 1 1 1 1 1
min = 1
max = 1

min_sum =
max_sum = +1

current number: 2


"""