def IsAbundantNumber(Num):
    Sum = 0
    n = 1
    while n < Num:
        if Num % n == 0:
            Sum += n
        n += 1
        if Sum > Num:
            return 1
    return 0


AbundantNumbers = []
for i in range(12, 28124):
    if IsAbundantNumber(i):
        AbundantNumbers.append(i)
    if i % 2000 == 0:
        print 'Finding Abundant Numbers.  (' + str(i) + '/28124) complete...'

print AbundantNumbers[0:10]

Sum = 0
for n in range(1, 5): #Memory overload, cut to 4 steps
    SumOfTwoAbundantNumbers = []
    print 'Finding Sum Of Two AbundantNumbers. Step (' + str(n) + '/4)....'
    for i in AbundantNumbers:
        if i >= n * 7031:
            break
        
        for j in AbundantNumbers:
            if j < i:
                continue
            if i + j >= n * 7031:
                break
            if i + j < (n-1) * 7031:
                continue
            SumOfTwoAbundantNumbers.append(i + j)

    for i in range((n-1)*7031,n*7031):
        if not(i in SumOfTwoAbundantNumbers):
            Sum += i

    del SumOfTwoAbundantNumbers

print Sum
