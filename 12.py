Divisor_Count = 1
n = 0

while Divisor_Count <= 500:
    Divisor_Count = 1
    n += 1
    i = 1
    Num = (n + 1)*n/2

    PrimeList = []
    while Num != 1:
        i += 1
        PrimeCount = 0
        while Num % i == 0:
            Num /= i
            PrimeCount += 1
        PrimeList.append(PrimeCount)

    for p in PrimeList:
        Divisor_Count *= (p + 1)

    if n%1000==0:
        print 'please wait. checking ' + str(n) + 'th number...'

print (n + 1)*n/2
