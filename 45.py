def Triangle(n):
    return n * (n + 1) / 2

def Pentagonal(n):
    return n * (3 * n - 1) / 2

def Hexagonal(n):
    return n * (2 * n - 1)

T = 285
P = 165 + 1
H = 143 - 1

def HexagonalANDPentagonal():
    global H, P
    while Hexagonal(H) > Pentagonal(P):
        P += 1

def PentagonalANDTriangle():
    global P, T
    while Pentagonal(P) > Triangle(T):
        T += 1
while Hexagonal(H) != Pentagonal(P) or Pentagonal(P) != Triangle(T):
    if Hexagonal(H) == Pentagonal(P):
        PentagonalANDTriangle()
        if Pentagonal(P) == Triangle(T):
            print Triangle(T)
            break
    else:
        H += 1
        HexagonalANDPentagonal()
