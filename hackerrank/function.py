def is_leap(y):
    if y < 1900 or y > 10 ** 5:
        return False

    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
        else:
            return True

    return False


year = int(input())
print(is_leap(year))

