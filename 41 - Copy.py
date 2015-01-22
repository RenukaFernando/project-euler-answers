Primes = []
n = 2
while n < 10**10:
    
    if n % 100000 == 0:
        print 'Find primes. (' + str(n/100000) + '/100000)'
    Prime = True
    for i in Primes:
        if i > n**0.5:
            break
        if n % i == 0:
            Prime = False
            break
    if Prime:
        Primes.append(n)

    n += 1
