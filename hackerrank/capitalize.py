# https://www.hackerrank.com/challenges/capitalize/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    if len(s) == 0 or len(s) > 1000:
        exit(1)

    lstr = list(s)
    res = ""
    in_word = False
    is_first = False
    is_done = False

    for i in range(0, len(s)):
        if s[i].isalnum():
            if in_word is False:
                in_word = True
            if is_first is False:
                is_first = True

            if in_word and is_first and is_done is False:
                if s[i].isalpha() and s[i].isupper() is False:
                    lstr[i] = chr(ord(lstr[i]) - 32)
                    is_first = False
                is_done = True
        else:
            if in_word:
                in_word = False
                is_first = False
                is_done = False

    res = res.join(lstr)

    return res


if __name__ == '__main__':
    s = input()
    result = solve(s)


