#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def solution_one(candles: list[int]) -> int:
    tallest = max(candles)
    tallest_count = candles.count(tallest)

    return tallest_count

def solution_two(candles: list[int]) -> int:
    tallest = 0
    count = 0
    
    for candle in candles:
        if candle > tallest:
            tallest = candle
    
    for candle in candles:
        if candle == tallest:
            count += 1
    
    return count

def birthdayCakeCandles(candles):
    # either of solution_one or solution_two
    result = solution_two(candles)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
