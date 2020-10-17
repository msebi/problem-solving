import numpy as np
np.set_printoptions(legacy='1.13')

line1 = np.array(input().split(' ')).astype(int)

n = line1[0]
m = line1[1]

mat = np.zeros((n, m)).astype(int)

for i in range(n):
    mat[i] = input().split(' ')

print(np.prod(np.sum(mat, axis=0)))


