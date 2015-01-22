Pandigital = []
a = 2
'''
ways
digist count of
a   b   a*b
1   4   4
2   3   4
'''
while a < 100:
    if a < 10:
        b = 1234
        bb = 9876
    else:
        b = 123
        bb = 987

    if a % 10 == 0 or a % 11 == 0:
        a += 1
        continue

    while b < bb:
        NotPandigital = False
        for i in str(b):
            if i == '0' or i in str(a):
                NotPandigital = True
                break
            SameDigits = 0
            for j in str(b):
                if i == j:
                    SameDigits += 1
                if SameDigits == 2:
                    break
            if SameDigits == 2:
                    NotPandigital = True
                    break
        if NotPandigital:
            b += 1
            continue

        NotPandigital = False
        for i in str(a * b):
            if i == '0' or i in str(a) or i in str(b):
                NotPandigital = True
                break
            SameDigits = 0
            for j in str(a * b):
                if i == j:
                    SameDigits += 1
                if SameDigits == 2:
                    break
            if SameDigits == 2:
                NotPandigital = True
                break
        if NotPandigital:
            b += 1
            continue

        if not(a * b in Pandigital):
            Pandigital.append(a * b)

        b += 1
    a += 1
    

print sum(Pandigital)
