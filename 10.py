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
# 07:05:45PM 12:45:54PM


def timeConversion(s):
    # Write your code here
    return (f"{(int(s[0:2]) + 12) if int(s[0:2]) != 12 else s[0:2]}{s[2:len(s)-2]}") if (s[len(s)-2:]) == "PM" else (s[:len(s)-2]) if (s[0:2]) != "12" else (f"0{(int(s[0:2]) - 12)}{s[2:len(s)-2]}")


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
