# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?h_r=next-challenge&h_v=zen



# def print_rangoli(size):
#     for i in range(0, size * 2 - 1):
#         line = ""
#         for j in range(0, 4 * (size - 1) + 1):
#             if i < size:
#                 if j < size:
#                     line = line + chr(97 + n - i + 1)
#                     if j + 1 <= i * 2:
#                         line = line + '-'
#             elif i >= size:
#
#         print(line.center(size * 2 - 1 + size + 1, '-'))

tile = []


def print_rangoli(size):
    if size < 0 or size > 27:
        exit(1)

    line = ""
    for i in range(0, size):
        row_len = 2 * (size - i - 1)
        for j in range(0, row_len):
            line = line + "-"
        for j in range(0, i + 1):
            line = line + chr(97 + size - j - 1)
            if j < i:
                line = line + "-"
        tile.append(line)
        line = ""

    for str in tile:
        print(str + str[::-1][1:])

    for i in range(1, len(tile)):
        print(tile[len(tile) - i - 1] + tile[len(tile) - i - 1][::-1][1:])


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

