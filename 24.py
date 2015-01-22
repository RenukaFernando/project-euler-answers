def Factorial(n):
    if n == 0:
        return 1
    N = 1
    for i in range(2,n+1):
        N *= i
    return N

Numbers = range(0,10)
Number = ''

n = 1000000-1
for i in range(9, -1, -1):
    Factorial_i = Factorial(i)
    Number += str(Numbers[n/Factorial_i])
    del Numbers[n/Factorial(i)]
    n %= Factorial_i

print Number
