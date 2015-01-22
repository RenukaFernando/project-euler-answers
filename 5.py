Num = range(2, 21)

n = 1
Lst = []
Ku_Po_Gu = 1
while True:
    n += 1
    while True:
        if any(i % n == 0 for i in Num):
            for i in Num:
                if i % n == 0:
                    Lst.append(i / n)
                else:
                    Lst.append(i)
            Num = Lst[:]
            Lst = []
            Ku_Po_Gu *= n
        else:
            break

    if all(i == 1 for i in Num):
        break

print Ku_Po_Gu

    
