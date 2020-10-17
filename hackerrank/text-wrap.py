# https://www.hackerrank.com/challenges/text-wrap/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import textwrap
import os


def wrap(string, max_width):
    i = 0
    res = ""
    while len(string[i: i + max_width]) > 0:
        res = res + string[i: i + max_width] + os.linesep
        i = i + max_width
    return res


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

