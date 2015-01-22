L = []

for a in range(2, 101):
    for b in range(2, 101):
        L.append(a**b)

L.sort()
TermsCount = 1
for i in range(len(L) - 1):
    if L[i] != L[i + 1]:
        TermsCount += 1

print TermsCount
