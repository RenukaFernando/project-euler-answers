Primes = [2, 3, 7]
OddComposite = 9

def IsOddComposite(n):
    global Primes
    if any(n % i == 0 for i in Primes):
        return True
    else:
        Primes.append(n)
        return False

conjecture = True

OddComposite -= 2 #Because +2 in while
while conjecture:
    OddComposite += 2
    Prime = OddComposite - 2 * 1**2
    i = 1

    conjecture = False
    while not IsOddComposite(OddComposite):
        OddComposite += 2
    
    while Prime > 1:
        if Prime in Primes:
            #Next OddComposite
            conjecture = True
            break
        
        i += 1
        Prime = OddComposite - 2* i**2

print OddComposite
