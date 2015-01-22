PrimeFactors = []
Primes = [] # <---- 4-digit Primes

def IsPrime(n):
    global PrimeFactors
    for i in PrimeFactors:
        if n % i == 0:
            return False
    return True

'Find Prime Factors for finding Primes'
n = 2
while n <  32: #Here 32 is 1000**0.5
    if IsPrime(n):
        PrimeFactors.append(n)
    n += 1

'Find 4-digit Primes'
n = 1000
while n <  10000:
    if IsPrime(n) and not('1' in str(n) and '2' in str(n) and '3' in str(n)):
        Primes.append(n)
    n += 1

del PrimeFactors

def IsPermutation(n1, n2, n3):
    n1, n2, n3 = str(n1), str(n2), str(n3)
    for i in n1:
        if not(i in n2) or not(i in n3):
            return False
    else:
        for i in n2:
            if not(i in n1) or not(i in n3):
                return False
        else:
            for i in n3:
                if not(i in n1) or not(i in n2):
                    return False
            else:
                return True

Len = len(Primes)
#n1, n2, n3 is The Arithmetic Sequence
BreakAll = False
for n1 in Primes[0:-2]:
    IndexOfn1 = Primes.index(n1)
    if IndexOfn1 % 10 == 0:
        print 'Checking....\t', IndexOfn1, '/', Len
    
    for n2 in Primes[IndexOfn1 + 1:-1]:
        if BreakAll or n2 > (9999 + n1)/2:
            break
        for n3 in Primes[Primes.index(n1)+2:]:
            if n3 > 2 * n2 - n1:
                break
            if n3 == 2 * n2 - n1 and n1 != 1487 and IsPermutation(n1, n2, n3):
                print int(str(n1) + str(n2) + str(n3))
                BreakAll = True
                break
    if BreakAll:
        break
                
