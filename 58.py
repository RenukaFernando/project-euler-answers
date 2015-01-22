Numerator = 8
Denominator = 13

Primes = [2]
LastPrime = 2
def IsPrime(n):
    global Primes
    global LastPrime
    N = LastPrime
    while N < n ** 0.5:
        N += 1
        for i in Primes:
            if i > N ** 0.5:
                Primes.append(N)
                LastPrime = N
                break
            if N % i == 0:
                break
    for i in Primes:
        if n % i == 0:
            return False
    return True

length = 7
n = 49 #7**2
percent = 0.62

while percent >= 0.1:
    length += 2
    Denominator += 4

    for i in range(3):
        n += length - 1
        if IsPrime(n):
            Numerator += 1

    n += length - 1
    percent = float(Numerator)/Denominator

print length
