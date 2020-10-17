# https://www.hackerrank.com/challenges/designer-door-mat/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import math

if __name__ == '__main__':
    something = input()
    v = something.split()
    n = int(v[0])
    m = int(v[1])

    if n < 5 or n > 101:
        exit(1)

    if m < 15 or m > 303:
        exit(1)

    for i in range(0, n):
        if i == math.floor(n / 2):
            print("WELCOME".center(m, '-'))
        else:
            if i < math.floor(n / 2):
                print((".|." * (i * 2 + 1)).center(m, '-'))
            else:
                if i > math.floor(n / 2):
                    print((".|." * ((n - i - 1) * 2 + 1)).center(m, '-'))



