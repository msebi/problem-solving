# https://www.hackerrank.com/challenges/find-a-string/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def count_substring(string, sub_string):
    if len(string) > 200:
        return 0

    if string.find(sub_string) < 0:
        return 0

    k = 0
    for i in range(0, len(string)):
        if string.find(sub_string, i, i + len(sub_string)) >= 0:
            k = k + 1
    return k


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)




