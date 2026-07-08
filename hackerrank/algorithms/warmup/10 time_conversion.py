#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s) -> str:
    hour = s[:2]
    time_classification = s[-2::]
    minutes = s[2:8]

    if time_classification == "AM":
        if hour == "12":
            return f'00{minutes}'
        else:
            return f'{hour}{minutes}'

    if time_classification == "PM":
        if hour == "12":
            return f"12{minutes}"
        else:
            return f"{int(hour) + 12}{minutes}"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

