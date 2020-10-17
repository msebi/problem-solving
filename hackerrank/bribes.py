# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
# def minimumBribes(q):
#     k = 0
#     for i in range(len(q)):
#         t = abs(q[i] - i - 1)
#         if t > 2:
#             print('Too chaotic')
#             return
#         else:
#             k = k + t
#
#     print(int(k/2))


# def minimumBribes(q):
#     pairs = [None] * (len(q))
#     # python sucks ass
#     for i in range(len(q)):
#         q[i] = q[i] - 1
#
#     k = 0
#     for i in range(len(pairs)):
#         pairs[i] = q[i]
#
#     for i in range(len(pairs)):
#         if pairs[i] - pairs[pairs[i]] > 1:
#             print('Too chaotic')
#             return
#
#     for i in range(len(pairs)):
#         if pairs[i] > i:
#             k = k + pairs[i] - i
#
#     print(k)

# def minimumBribes(q):
#     tmp = [None] * len(q)
#     for i in range(0, len(tmp)):
#         tmp[i] = i + 1
#
#     k = 0
#     c_i = -1
#
#     for i in range(len(tmp)):
#         if q[i] > tmp[i]:
#             if q[i] - tmp[i] > 2:
#                 print('Too chaotic')
#                 return
#             k = k + (q[i] - tmp[i])
#             if c_i < 0:
#                 c_i = i
#                 continue
#             k = k + i - c_i - 1
#             c_i = i
#     print(k)

def minimumBribes(q):
    indexes = [None] * len(q)
    tmp = [None] * len(q)
    for i in range(0, len(indexes)):
        indexes[i] = i + 1
        tmp[i] = i + 1

    k = 0
    while indexes[k] == q[k] and k < len(q):
        k = k + 1

    q = q[k:len(q)]
    indexes = indexes[k:len(indexes)]
    tmp = tmp[k:len(tmp)]

    k = 0

    for i in range(len(q)):
        if tmp[i] != q[i]:
            if q[i] - indexes[i] > 2:
                print('Too chaotic')
                return

            for j in range(i+1, len(tmp)):
                if q[i] == tmp[j]:
                    aux = tmp[j]
                    for m in range(j, i, -1):
                        tmp[m] = tmp[m-1]
                    tmp[i] = aux
                    k = k + j - i
                    break

            # print('[%s]' % ', '.join(map(str, tmp)))
    print(k)


def test():
    n = 1
    k = [8]
    people = [
        [1, 2, 5, 3, 7, 8, 6, 4]
    ]

    for i in range(n):
        no = k[i]
        v = people[i]
        minimumBribes(v)


if __name__ == '__main__':
    test()
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)