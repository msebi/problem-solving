import numpy as np

A = np.array(input().split(' ')).astype(int)
B = np.array(input().split(' ')).astype(int)

print(np.inner(A, B))
print(np.outer(A, B))
