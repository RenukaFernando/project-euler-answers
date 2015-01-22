import math

def Permutate(n):
    Value = ''
    Dig = range(9, -1, -1)

    DecimalPlace = 10

    while DecimalPlace > 0:
        Nth = (n/math.factorial(DecimalPlace - 1))% DecimalPlace
        Value += str(Dig[Nth])
        del Dig[Nth]
        DecimalPlace -= 1

    return Value

n = 0
Sum = 0
while n < math.factorial(10):
    #show progress
    if n % 100000 == 0:
        print "Calculating...", n ,"/3628800"
    
    Val = Permutate(n)

    HaveDivisibilityProperty = int(Val[1:4]) % 2 == 0
    HaveDivisibilityProperty = HaveDivisibilityProperty and int(Val[2:5])  % 3  == 0
    HaveDivisibilityProperty = HaveDivisibilityProperty and int(Val[3:6])  % 5  == 0
    HaveDivisibilityProperty = HaveDivisibilityProperty and int(Val[4:7])  % 7  == 0
    HaveDivisibilityProperty = HaveDivisibilityProperty and int(Val[5:8])  % 11 == 0
    HaveDivisibilityProperty = HaveDivisibilityProperty and int(Val[6:9])  % 13 == 0
    HaveDivisibilityProperty = HaveDivisibilityProperty and int(Val[7:10]) % 17 == 0

    if HaveDivisibilityProperty:
        Sum += int(Val)
    
    n += 1

print Sum
