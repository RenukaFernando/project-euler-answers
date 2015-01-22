Tot = 1
prime = 1

def IsPrime(Num):
    for i in range(2,Num):
        if Num % i == 0:
            return 0
    return 1

def NextPrime():
    global prime
    prime += 1
    while not IsPrime(prime):
        prime += 1

def Count():
    global prime
    Factor = 1
    while Factor <= 10:  #10
        Factor *= prime
    Factor /= prime
    return Factor

while prime <= 10:       #10
    NextPrime()
    if prime <= 10:
        Tot *= Count()

print Tot
