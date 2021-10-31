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


def diagonalDifference(arr):
    # Write your code here
    a = 0
    b = 0
    # for i in range(len(arr):-1):
    #     for j in
    for i, x in enumerate(range(len(arr), 0, -1)):
        a = a + arr[i][i]
        b = b + arr[i][x-1]

    return abs(a-b)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
