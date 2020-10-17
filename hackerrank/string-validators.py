# https://www.hackerrank.com/challenges/string-validators/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    s = input()
    if len(s) == 0 or len(s) > 1000:
        print(False)

    good = False

    for i in range(0, len(s)):
        if s[i].isalnum():
            good = True
            print(True)
            break

    if good is False:
        print(False)
    good = False

    for i in range(0, len(s)):
        if s[i].isalpha():
            good = True
            print(True)
            break

    if good is False:
        print(False)
    good = False

    for i in range(0, len(s)):
        if s[i].isdigit():
            good = True
            print(True)
            break

    if good is False:
        print(False)
    good = False

    for i in range(0, len(s)):
        if s[i].islower():
            good = True
            print(True)
            break

    if good is False:
        print(False)
    good = False

    for i in range(0, len(s)):
        if s[i].isupper():
            good = True
            print(True)
            break

    if good is False:
        print(False)
    good = False




