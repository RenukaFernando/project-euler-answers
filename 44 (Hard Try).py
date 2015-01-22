Lst = []
def T(N):
    return N*(3*N - 1)/2

def IsDifferencePentagonal(N):
    global Lst
    Lst = []
    n1 = N
    n2 = N+1

    TN = T(N)
    Tn2 = T(n2)
    Tn1 = T(n1)
    
    while TN >= Tn2 - Tn1 or n2 != n1 + 1:
        
        if TN == Tn2 - Tn1:
            Lst.append([Tn1,Tn2])

        n1 -= 1
        Tn1 = T(n1)
        
        if TN < Tn2 - Tn1:
            n1 = n2
            n2 += 1
            Tn1 = T(n1)
            Tn2 = T(n2)

def IsPentagonal(Values):
    for N1N2 in Values:
        Value = N1N2[0] + N1N2[1]
        n = round((2*Value/3)**0.5,0)
        if T(n) == Value:
            return True
    return False

P = 1

while IsDifferencePentagonal(P) == [] or not IsPentagonal(Lst):
    if P % 10 == 0:
        print "Checking", P, "th term is the difference....."
    P += 1

print T(P) #Solution is 1912 th one.
