a = 998
b = 1
c = 1

def abc():
    global a, b, c
    while True:
        while b > c:
            if a <= b:
                b -= 1
                c += 1
                continue
            if a**2 == b**2 + c**2:
                return a*b*c
            b -= 1
            c += 1
        a -= 1
        b = 999 - a
        c = 1

print abc()
