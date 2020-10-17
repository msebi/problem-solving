
a = int(input())
b = int(input())
m = int(input())



def mypow(a, b, m = 1):
    print(a ** b)
    print(a ** b % m)


mypow(a, b, m)
