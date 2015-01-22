Max = 9**6

i = 2
SumOfFifthPower = 0
while i <= Max:
    if i%50000 == 0:
        print 'wait. (' + str(i) + '/' + str(Max) + ')'
    Sum = 0
    for digit in str(i):
        Sum += int(digit)**5
    if Sum == i:
        SumOfFifthPower += i
    i += 1

print SumOfFifthPower
