Max = 2540160 #= 9!9!9!9!9!9!9! (9!9!9!9!9!9!9! > 2540160)

Fac = 1
Factorial = [1]
for i in range(1, 10):
    Fac *= i
    Factorial.append(Fac)

Sum = 0

for n in range(10, Max + 1):
    if n % 500000 == 0:
        print 'Wait. ' + str(n) + '/' + str(Max)
    Val = 0
    for i in str(n):
        Val += Factorial[int(i)]
    if n == Val:
        Sum += n

print Sum
