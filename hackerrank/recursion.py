import itertools


chars = ['a', 'b', 'c']
fstr = ""


def recursion(slen, index):
    global fstr
    if index == slen:
        print(fstr)
        fstr = ""
        return

    for i in range(0, index):
        if chars[i] != chars[index]:
            fstr = fstr + chars[i]
            recursion(slen, index + 1)


if __name__ == '__main__':
    recursion(3, 1)

    # print(list(itertools.permutations(chars)))

