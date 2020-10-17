import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print('Weird')
        exit()
    if 2 <= n <= 5:
        print('Not Weird')
        exit()
    if 6 <= n <= 20:
        print('Weird')
        exit()
    if n > 20:
        print('Not Weird')
