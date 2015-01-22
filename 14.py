def NextTerm(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

def Sequence():
    global Num, L
    L = [Num]
    while True:
        Num = NextTerm(Num)
        '''
        for i in L:
            if i == Num:
                return
        '''
        if Num == 1:
            return
        L.append(Num)

Num = 1
n = 1
L = []
MaxTerms_Count = 0
StartingNum = 1

while n < 1000000:
    Num = n
    Sequence()
    if len(L) > MaxTerms_Count:
        MaxTerms_Count = len(L)
        StartingNum = n

    if n % 10000 == 0:
        print 'Plz wait ' + str(n / 10000) + '% complete...'
    n += 1

print StartingNum
