def IsPermutation(n1, n2):
    n1, n2 = str(n1), str(n2)

    if len(n1) != len(n2):
        return False

    N1 = []
    for digit in n1:
        N1.append(digit)

    for digit in n2:
        if digit in N1:
            del N1[N1.index(digit)]
    if len(N1) != 0:
        return False
    else:
        return True

n = 1
while True:    
    if IsPermutation(n, 2*n) and IsPermutation(2*n, 3*n) and IsPermutation(3*n, 4*n) and IsPermutation(4*n, 5*n) and IsPermutation(5*n, 6*n):
        print n
        break

    n += 1
