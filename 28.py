Sum = 1

n = 1
add = 2
while add + 1 <= 1001:
    N = []
    for i in range(4):
        n += add
        N.append(n)
    Sum += sum(N)
    add += 2

print Sum
