f = open("18.txt")
lst = []

for i in range(15):
    lst.append(f.readline().split())

MaxVal = 0
for a in range(2):
    for b in range(a, a+2):
        for c in range(b, b+2):
            for d in range(c,c+2):
                for e in range(d,d+2):
                    for f in range(e,e+2):
                        for g in range(f,f+2):
                            for h in range(g,g+2):
                                for i in range(h,h+2):
                                    for j in range(i,i+2):
                                        for k in range(j,j+2):
                                            for l in range(k,k+2):
                                                for m in range(l,l+2):
                                                    for n in range(m,m+2):
                                                        Val = int(lst[0][0])+int(lst[1][a])+int(lst[2][b])+int(lst[3][c])+int(lst[4][d])+int(lst[5][e])+int(lst[6][f])+int(lst[7][g])+int(lst[8][h])+int(lst[9][i])+int(lst[10][j])+int(lst[11][k])+int(lst[12][l])+int(lst[13][m])+int(lst[14][n])
                                                        if Val > MaxVal:
                                                            MaxVal = Val

print MaxVal
