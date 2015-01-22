'3/2 --> 3+2+2/3+2 = 7/5 --> 7+5+5/7+5 = 17/12 --> 17+12+12/17+12 = 41/29'
'(1)            (2)                 (3)                         (4)'

n = 1
count = 0

Numerator = 3
Denominator = 2
while n <= 1000:
    if len(str(Numerator)) > len(str(Denominator)):
        count += 1
    
    Numerator += 2*Denominator
    Denominator = Numerator - Denominator
    n += 1

print count
