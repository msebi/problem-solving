import numpy as np

# Seems quite useful
# https://www.hackerrank.com/challenges/np-polynomials/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Creates a list with comma separated elements
coef = list(map(float, input().split()))
val = float(input())

# print(coef)
# print(val)

print(np.polyval(coef, val))





