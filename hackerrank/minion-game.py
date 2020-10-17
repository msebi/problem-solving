# https://www.hackerrank.com/challenges/the-minion-game/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


def gen_words(player, vow, con, s):
    words = []

    # Sliding window
    if player:
        # A
        words.extend(vow)
        for w_len in range(1, len(s) + 1):
            for i in range(0, len(vow)):
                for j in range(0, len(s)):
                    if s[j] == vow[i]:
                        if j > len(s) or j + w_len > len(s):
                            break
                        if s[j:j + w_len] not in words:
                            words.append(s[j:j + w_len])
                            break
    else:
        # B
        words.extend(con)
        for w_len in range(1, len(s) + 1):
            for i in range(0, len(con)):
                for j in range(0, len(s)):
                    if s[j] == con[i]:
                        if j > len(s) or j + w_len > len(s):
                            break
                        if s[j:j + w_len] not in words:
                            words.append(s[j:j + w_len])
                            break

    return words


def search_word(w, s):
    k = 0
    i = 0

    while i < len(s):
        curr = s.find("".join(w), i)
        if curr == -1:
            return k
        i = curr + 1
        k = k + 1

    return k


def count_word(w, s):
    k = 0

    for i in range(0, len(w)):
        k = k + search_word(w[i], s)

    return k


# def minion_game(s):
#     if len(s) == 0 or len(s) > pow(10, 6):
#         exit(1)
#
#     vowels = "AEIOU"
#     g_vow = []
#     g_con = []
#     s_a = 0
#     s_b = 0
#
#     for i in range(0, len(s)):
#         if s[i] in vowels and s[i] not in g_vow:
#             g_vow.append(s[i])
#         elif s[i] not in vowels and s[i] not in g_con:
#             g_con.append(s[i])
#
#     words_a = gen_words(True, g_vow, g_con, s)
#     words_b = gen_words(False, g_vow, g_con, s)
#
#     s_a = count_word(words_a, s)
#     s_b = count_word(words_b, s)
#
#     if s_a > s_b:
#         print("Kevin " + str(s_a))
#     else:
#         print("Stuart " + str(s_b))

def minion_game(s):
    vow = "AEIOU"

    s_a = 0
    s_b = 0

    for i in range(len(s)):
        if s[i] in vow:
            s_a = s_a + len(s) - i
        else:
            s_b = s_b + len(s) - i

    if s_a > s_b:
        print("Kevin " + str(s_a))
    elif s_b > s_a:
        print("Stuart " + str(s_b))
    else:
        print("Draw")

if __name__ == '__main__':
    # s = input()
    s = "BAANANAS"
    minion_game(s)



