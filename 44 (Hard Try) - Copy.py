Tn1 = 1
Tn2 = 5

def T(N):
    return N*(3*N - 1)/2

def IsDifferencePentagonal(N):
    global Tn1, Tn2
    n1 = N
    n2 = N+1

    TN = T(N)
    Tn2 = T(n2)
    Tn1 = T(n1)
    
    while TN >= Tn2 - Tn1 or n2 != n1 + 1:
        
        if TN == Tn2 - Tn1:
            return True

        n1 -= 1
        Tn1 = T(n1)
        
        if TN < Tn2 - Tn1:
            n1 = n2
            n2 += 1
            Tn1 = T(n1)
            Tn2 = T(n2)
        
    return False

def IsPentagonal(Value):
    n = round((2*Value/3)**0.5,0)
    return T(n) == Value

P = 1
while not IsDifferencePentagonal(P) or not IsPentagonal(Tn1 + Tn2):
    if P % 10 == 0:
        print "Checking", P, "th term is the difference....."
    P += 1

print T(P) #Solution is 1912 th one.
#This is incorrect when TN = Tn2 - Tn1 = Tn4 - Tn3;
#Here Tn4, Tn3 are another answer. it is not found by IsDifferencePentagonal Function
