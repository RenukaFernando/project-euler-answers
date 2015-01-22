Sum = 0
Num = 2
PrimeList = []

def IsPrime(Num):
    return not any(Num % i == 0 for i in PrimeList)

while Num < 2000000:
    if IsPrime(Num):
        PrimeList.append(Num)
        Sum += Num
    if Num % 20000 == 0:
        print 'Plz wait ' + str(Num/20000) + '% complete...'
    Num += 1

print Sum
