#Find Primes
print 'Find Primes'
Primes = []
n = 2

def IsPrime(n):
    global Primes
    N = n**0.5
    for i in Primes:
        if n % i == 0:
            return False
        if i > N:
            return True
    return True

while n < 1000000:
    if IsPrime(n):
        Primes.append(n)
    n += 1

Len = len(Primes)
print 'Completed. Primes Count =', Len
#End Find Primes

P, p = 2, 0
i = 0
Terms = 0
MaxTerms, ThePrime = 0, 0

while p <= Len:
    if p % 1000 == 0:
        print 'Complete...\t', p, '/', Len
    
    Sum = 2
    i, j = 0, 1
    while Primes[i] <= P:
        Sum = sum(Primes[i:j])
        while Sum <= P:
            if Sum == P:
                Terms = j - i
                if MaxTerms < Terms:
                    MaxTerms = Terms
                    ThePrime = P
            j += 1
            Sum = sum(Primes[i:j])
        i += 1
        if MaxTerms > j - i:
            break
    p += 1
    if p < Len:
        P = Primes[p]

print '\nPrimes Count =', MaxTerms,'\nThe Prime =', ThePrime
