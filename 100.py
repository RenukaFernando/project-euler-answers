Total, T, B = 10**12, 0, 1
Sqrt2 = 2**0.5
while T != B:
    if Total % 100 == 0:
        print T, B

    D = (B - T)/2
    Total += D
    Blue = round(Total/Sqrt2, 0)

    while T != B:
        Total += 1
        Blue = round(Total/Sqrt2, 0)
        B = 2*Blue*(Blue-1)
        T = Total*(Total-1)

    B = 2*Blue*(Blue-1)
    T = Total*(Total-1)

print int(Blue)
