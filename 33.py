def Convert(n):
    if n == 0:
        return 1
    else:
        return 0

A = 1
B = 1

for a in range(11, 99):
    if a % 10 == 0:
        continue #remove 0 from a
    for b in range(a + 1, 100):
        if b % 10 == 0:
            continue #remove 0 from b
        
        for i in range(2):
            for j in range(2):
                if str(a)[i] == str(b)[j]:
                    if (a*float(str(b)[Convert(j)]))/(b*float(str(a)[Convert(i)])) == 1:
                        A *= a
                        B *= b

n = 2
while n <= A:
    while A % n == 0 and B % n == 0:
        A /= n
        B /= n
    n += 1

print B
