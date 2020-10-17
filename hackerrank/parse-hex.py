# https://www.hackerrank.com/challenges/hex-color-code/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen#

import re

open_str = False
k = 0
pattern = re.compile("#(?:[0-9a-fA-F]{3}){1,2}")


def parse_hex(s):
    global open_str, k

    if open_str is False:
        j = s.find('}')
        if j >= 0:
            return

        j = s.find('{')
        if j < 0:
            return

        open_str = True
        k = k + 1
        if j + 1 < len(s):
            parse_hex(s[j+1:])
            li = s.find('}')
            if li >= 0:
                open_str = False
                k = k - 1
                for strs in re.findall(pattern, s[:li]):
                    print(strs)
    else:
        j = s.find('}')
        if j >= 0:
            open_str = False
            k = k - 1
            for strs in re.findall(pattern, s[:j]):
                print(strs)
            return

        j = s.find('{')
        if j > 0:
            if j + 1 < len(s):
                parse_hex(s[j + 1:])
                li = s.find('}')
                if li >= 0:
                    open_str = False
                    k = k - 1
                    for strs in re.findall(pattern, s[:li]):
                        print(strs)
                    return

        for strs in re.findall(pattern, s):
            print(strs)


def run_test():
    s = "#BED \n" \
        "{ \n" \
        "            color: #FfFdF8; background-color:#aef; \n" \
        "            font-size: 123px; \n" \
        "            background: -webkit-linear-gradient(top, #f9f9f9, #fff); \n" \
        "} \n" \
        "#Cab \n " \
        "{ \n" \
        "           background-color: #ABC; \n" \
        "           border: 2px dashed #fff; \n" \
        "} \n"

    strs = s.splitlines()
    for st in strs:
        parse_hex(st)


def test_regex():
    reg = "            color: #FfFdF8; background-color:#aef; \n"
    # reg = "#FfFdF8; background-color:#aef; \n"
    # reg = "#FFF"
    for strs in re.findall(pattern, reg):
        print(strs)


if __name__ == '__main__':
    # test_regex()
    # run_test()
    n = int(input())
    for i in range(0, n):
        line = input()
        parse_hex(line)
