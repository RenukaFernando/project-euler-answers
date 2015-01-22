def IsPalindromic(n):
    N = ''
    for i in reversed(str(n)):
        N += i
    if str(n) == N:
        return 1
    return 0

Sum = 0
for n in range(1000000):
    if n % 500000 == 0:
        print 'Wait. (' + str(n) + '/999999)...'
    if not(IsPalindromic(n)):
        continue

    if IsPalindromic(bin(n)[2:]):
        Sum += n

print Sum
