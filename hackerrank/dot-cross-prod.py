import numpy as np

n = int(input())

A = np.zeros((n, n)).astype(int)
B = np.zeros((n, n)).astype(int)

for i in range(n):
    A[i] = input().split(' ')

for i in range(n):
    B[i] = input().split(' ')

# print(A)
# print(B)

print(np.dot(A, B))


