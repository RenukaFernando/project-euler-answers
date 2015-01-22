Num = 600851475143
n = 1
while Num != 1:
    n += 1
    while Num % n == 0:
        Num /= n

print n
