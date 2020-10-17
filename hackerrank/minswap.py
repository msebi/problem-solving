import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
# def minimumSwaps(arr):
#     res = 0
#
#     for i in range(len(arr)):
#         arr[i] = arr[i] - 1
#
#     i_front = {}
#     i_rev = {}
#     for i in range(len(arr)):
#         i_front[i] = arr[i]
#
#     for i in range(len(i_front)):
#         i_rev[i_front[i]] = i
#
#     for i in range(len(arr)):
#         if i_front[i] != i:
#             i_front[i] = i_rev[i_front[i]]
#             res = res + 1
#
#     return res - 1


def minimumSwaps(arr):
    res = 0

    for i in range(len(arr)):
        if arr[i] != i + 1:
            arr[i] = arr[arr[i] - 1]
            res = res + 1

    return res


def test():
    # test_arr = [7, 1, 3, 2, 4, 5, 6]
    test_arr = [4, 3, 1, 2]
    minimumSwaps(test_arr)


if __name__ == '__main__':
    # test()
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)




