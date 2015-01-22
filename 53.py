from math import factorial

def nCr(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

def IsEven(n):
    return n % 2 == 0

n = 23
Count = 0
while n <= 100:
    r = 0
    while r <= n/2:
        if nCr(n, r) > 1000000:
            Count += n + 1 - 2*r
            break
        r += 1
    n += 1

print Count
