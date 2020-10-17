# https://www.hackerrank.com/challenges/python-string-formatting/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def print_formatted(number):
    if number < 1 or number > 100:
        exit(1)

    width = len("{0:b}".format(number))
    for i in range(1, n + 1):
        print("{0:{blah}d} {0:{blah}o} {0:{blah}X} {0:{blah}b}".format(i, blah=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

