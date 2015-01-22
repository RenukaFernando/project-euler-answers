MaxSols = 0
for p in range(3, 1001):
    if p % 100 == 0:
        print 'Wait. (' + str(p) + '/1000)...'
    Sols = 0
    for a in range(p-2, 0, -1):
        b = p - a - 1
        c = 1        
        while b >= c:
            if a < b:
                b -= 1
                c += 1
                continue
            if a**2 == b**2 + c**2:
                Sols += 1
            b -= 1
            c += 1
            
    if Sols > MaxSols:
        MaxSols = Sols
        P = p

print P
