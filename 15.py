#Answer is 40!/(20!20!)
Ans = 1

for i in range(21,41):
    Ans *= i

for j in range(1, 21):
    Ans /= j

print Ans
