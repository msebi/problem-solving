import numpy as np
np.set_printoptions(legacy='1.13')

size = input().split(" ")
n = int(size[0])
m = int(size[1])

mat = np.zeros((n, m))

for i in range(n):
    mat[i] = input().split(" ")


my_array = np.array(mat)

print(np.mean(my_array, axis=1))
print(np.var(my_array, axis=0))
print(np.std(my_array, axis=None))







