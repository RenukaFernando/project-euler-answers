def LeftToRight(n):
    return [int(str(n)[i:]) for i in range(1, len(str(n)))]

def RightToLeft(n):
    return [int(str(n)[:i]) for i in range(len(str(n)) - 1, 0, -1)]

def IsPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1

Term = 1
n = 23
Sum = 0
MainPrimes = [2, 3, 5, 7]

while Term < 12:
    if n % 10000 == 0:
        print 'Wait. Checking', n
    if not(int(str(n)[0]) in MainPrimes) or not(int(str(n)[len(str(n)) - 1]) in MainPrimes):
        n += 1
        continue
    if any(not IsPrime(i) for i in reversed(LeftToRight(n))):
        n += 1
        continue
    if any(not IsPrime(i) for i in reversed(RightToLeft(n))):
        n += 1
        continue
    if not IsPrime(n):
        n += 1
        continue

    Sum += n
    print 'Wait. (' + str(Term) + '/11)'
    n += 1
    Term += 1

print Sum
