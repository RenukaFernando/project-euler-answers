def IsPrime(Num):
    return all(Num % n != 0 for n in range(2, Num))

PrimeList = []
for i in range(1000):
    if IsPrime(i):
        PrimeList.append(i)

def Quadratic(a, b, n):
    if IsPrime(n**2 + a*n + b):
        return True
    else:
        return False

A = 0
B = 0
MaxPrimeCount = 0
step = 0 #to show process
for b in PrimeList:
    step += 1 #to show process
    print 'Please wait. (' + str(step) + '/' + str(len(PrimeList)) + ')...' #to show process
    a = -1000
    while a < 1000:
        n = 0
        PrimeCount = 0
        while Quadratic(a, b, n):
            PrimeCount += 1
            n += 1
        if PrimeCount > MaxPrimeCount:
            MaxPrimeCount = PrimeCount
            A = a
            B = b
        a += 1

print A*B
