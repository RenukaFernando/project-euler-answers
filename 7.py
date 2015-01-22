prime = 1
nthPrime = 10001

def IsPrime(Num):
    for i in range(2,Num):
        if Num % i == 0:
            return 0
    return 1

n = 0
while n < nthPrime:
    n += 1
    prime += 1
    if n%1000 == 0:
        print 'wait', 11 - n/1000
    while not IsPrime(prime):
        prime += 1

print prime #104713
    
