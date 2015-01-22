Primes = [2, 3]
No = 647

def FindPrimes(till):
    global Primes
    Last = Primes[len(Primes) - 1] + 2
    while Last <= till:
        if all(Last % i != 0 for i in Primes):
            Primes.append(Last)
        Last += 2

def HaveFourDistinctPrimeFactors(No):
    FindPrimes(No / 30) # Here 30 = 2*3*5; No = 2*3*5*x; here x may be the max prime.
    global Primes
    FactorsCount = 0
    
    for i in Primes:
        if No % i == 0:
            FactorsCount += 1
        if FactorsCount > 4:
            return False
    if FactorsCount == 4:
        return True
    else:
        return False

while True:
    Back = 0
    Front = 0
    if HaveFourDistinctPrimeFactors(No):
        for i in range(1,4):
            if HaveFourDistinctPrimeFactors(No - i):
                Back += 1
            else:
                break

        for i in range(1,4):
            if HaveFourDistinctPrimeFactors(No + i):
                Front += 1
            else:
                break

        if Back + Front >= 3:
            print No - Back
            break

    No += 4
