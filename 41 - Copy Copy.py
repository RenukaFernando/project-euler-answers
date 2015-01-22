n = 10**10
while True:
    n -= 1
    if n % 10 == 0:
        print 'Find primes. (' + str(n) + '/10000000000)'
    
    Break = False
    for i in range(1, len(str(n))+1):
        if not str(i) in str(n):
            Break = True
            break
    if Break:
        n -= 1
        continue
    
    Prime = True
    i = 2
    while i <= n**0.5:
        Prime = True
        if n % i == 0:
            Prime = False
            break
    if Prime:
        print Prime
        break

    n -= 1
