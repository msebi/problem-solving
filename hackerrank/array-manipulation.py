import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
# works but not optimal; getting time out error
def arrayManipulation(n, queries):
    res = 0
    c_max = 0
    c_sum = [None] * n
    for i in range(n):
        c_sum[i] = 0

    # queries has three elements [a, b, quantity]
    for q in queries:
        start_i = q[0] - 1
        stop_i = q[1]
        for i in range(start_i, stop_i):
            c_sum[i] = c_sum[i] + q[2]

    for i in range(n):
        if c_sum[i] >= c_max:
            c_max = c_sum[i]

    return c_max


def run_test():
    n = 10
    queries = [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]

    arrayManipulation(n, queries)


if __name__ == '__main__':
    run_test()
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
