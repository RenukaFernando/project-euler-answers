Prime = []
CircularPrimes = []
for n in range(2, 1000000):
    if n % 20000 == 0:
        print 'Find Primes. (' + str(n) + '/999999)'
    for i in Prime:
        if n % i == 0:
            break
    else:
        Prime.append(n)
        if n <= 100:
            continue
        for i in str(n):
            if not(i in '1379'):
                break
        else:
            CircularPrimes.append(n)

def Rotate(n):
    Rotations = []
    for i in range(0, len(str(n))):
        Rot = ''
        for j in range(0, len(str(n))):
            x = i + j
            if i + j >= len(str(n)):
                x = (i + j) % len(str(n))
            Rot += str(n)[x]
        Rotations.append(int(Rot))
    return Rotations

CircularPrimesCount = 13
for i in CircularPrimes:
    if i % 100 == 0:
        print 'Find Circular Primes. (' + str(i) + '/' + str(len(CircularPrimes)) + ')'
    IsCircularPrimes = True
    for j in Rotate(i):
        if j in CircularPrimes:
            del CircularPrimes[CircularPrimes.index(j)]
        else:
            IsCircularPrimes = False
    if IsCircularPrimes:
        CircularPrimesCount += len(Rotate(i))

print CircularPrimesCount

