n = 1
for i in range(1,101):
    n *= i

Sum = 0
for i in str(n):
    Sum += int(i)

print Sum
