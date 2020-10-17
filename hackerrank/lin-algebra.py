import numpy as np
np.set_printoptions(legacy='1.13')

n = int(input())

A = np.zeros((n, n)).astype(float)

for i in range(n):
    A[i] = input().split(' ')

print(np.linalg.det(A))

