# for i in range(1, int(input())):
#     print(''.join(str(i) * i))
#
# for i in range(1, int(input())):
#     print(sum([i * (10 ** j) for j in range(i)]))

for i in range(1, int(input())):
    print(int(i * 10 / 9 * 10 ** (i - 1)))
