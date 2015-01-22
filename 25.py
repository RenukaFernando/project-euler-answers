F1 = 1
F2 = 1

term = 2
while F2 < 10**999:
    x = F2
    F2 += F1
    F1 = x
    term += 1

print term
