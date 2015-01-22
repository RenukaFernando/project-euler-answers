def Sum_EvenlyDevice(Num):
    Sum = 0
    n = 1
    while n < Num:
        if Num % n == 0:
            Sum += n
        n += 1
    return Sum

AmicableNumber = 0

def IsAmicableNumber(Num):
    global AmicableNumber
    AmicableNumber = Sum_EvenlyDevice(Num)
    if AmicableNumber == Num:
        return 0
    if Num == Sum_EvenlyDevice(AmicableNumber):
        return 1
    else:
        return 0

Numbers = range(1,10000)
Sum = 0

for Num in Numbers:
    if IsAmicableNumber(Num):
        Sum += Num
        if AmicableNumber < 10000:
            Sum += AmicableNumber
            del Numbers[Numbers.index(AmicableNumber)]
    if Num % 1000 == 0:
        print 'please wait ' + str(Num / 100) + '% complete...'

print Sum
        
