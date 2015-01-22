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

print 'Step 1/2'
AbundantNumbers = []
for i in range(12, 28124):
    if IsAbundantNumber(i):
        AbundantNumbers.append(i)
    if i % 2000 == 0:
        print 'Finding Abundant Numbers.  (' + str(i) + '/28124) complete...'

Sum = 0
SumOfTwoAbundantNumbers = []

for i in AbundantNumbers:    
    for j in AbundantNumbers:
        if j < i:
            continue
        if i + j > 28123:
            break
        SumOfTwoAbundantNumbers.append(i + j)

SumOfTwoAbundantNumbers.sort()
n = 0
print 'Step 2/2'
for i in range(0, len(SumOfTwoAbundantNumbers)):
    if i % 2000000 == 0:
        print 'Finding Sum.  (' + str(i) + '/' + str(len(SumOfTwoAbundantNumbers)) +') complete...'
    for j in range(n + 1, SumOfTwoAbundantNumbers[i]):
        Sum += j
    n = SumOfTwoAbundantNumbers[i]

print Sum
