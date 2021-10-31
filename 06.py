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


def plusMinus(arr):
    # Write your code here
    # positive = 0
    # negetive = 0
    # zero = 0
    # for i in range(len(arr)):
    #     if arr[i] > 0:
    #         positive = positive + 1
    #     elif arr[i] < 0:
    #         negetive = negetive + 1
    #     else:
    #         zero = zero + 1

    # print(format((positive/len(arr)), '.6f'))
    # print(format((negetive/len(arr)), '.6f'))
    # print(format((zero/len(arr)), '.6f'))

    print(format(len([x for x in arr if x > 0])/n, ".6f"))
    print(format(len([x for x in arr if x < 0])/n, ".6f"))
    print(format(len([x for x in arr if x == 0])/n, ".6f"))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
