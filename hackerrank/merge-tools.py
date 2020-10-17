# https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen


def merge_the_tools(s, k):
    n_elem = int(len(s) / k)
    for i in range(0, n_elem):
        alphas = {"A": 1, "B": 1,
                  "C": 1, "D": 1,
                  "E": 1, "F": 1,
                  "G": 1, "H": 1,
                  "I": 1, "J": 1,
                  "K": 1, "L": 1,
                  "M": 1, "N": 1,
                  "O": 1, "P": 1,
                  "Q": 1, "R": 1,
                  "S": 1, "T": 1,
                  "U": 1, "V": 1,
                  "W": 1, "X": 1,
                  "Y": 1, "Z": 1}
        res = []
        for j in range(i * k, (i + 1) * k):
            if alphas[s[j]] > 0:
                res.append(s[j])
                alphas[s[j]] = 0
        print("".join(res))

    return


if __name__ == '__main__':
    # string, k = input(), int(input)
    string = "AABCAAADA"
    k = 3
    merge_the_tools(string, k)


