import math

def Permutate(Digits, n):
    Value = ''
    Dig = range(Digits, 0, -1)

    DecimalPlace = Digits

    while DecimalPlace > 0:
        Nth = (n/math.factorial(DecimalPlace - 1))% DecimalPlace
        Value += str(Dig[Nth])
        del Dig[Nth]
        DecimalPlace -= 1

    return int(Value)

def IsPrime(n):
    global Primes
    for i in Primes:
        if n % i == 0 and i**2 <= n:
            return False
    return True

#Find Primes under 10^5
Primes = [2,3]
n = 5
while n < 10**5:
    for i in Primes:
        if n % i == 0:
            break
        if i**2 >= n:
            Primes.append(n)
            break
    else:
        Primes.append(n)
    n += 2

Digits = 9
Breaked = False
while Digits > 0:
    DecimalPlace = Digits
    n = 0
    while n < math.factorial(DecimalPlace):
        if IsPrime(Permutate(Digits, n)):
            print Permutate(Digits, n)
            Breaked = True
            break
        n += 1

    if Breaked:
        break
    Digits -= 1
