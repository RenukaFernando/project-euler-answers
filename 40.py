A = ''
i = 1
while len(A) < 1000001:
    A += str(i)
    i += 1

print int(A[0])*int(A[9])*int(A[99])*int(A[999])*int(A[9999])*int(A[99999])*int(A[999999])
