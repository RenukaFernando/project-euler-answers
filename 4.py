def IsPalindromicNumber(Num):
    Digits = []
    for digit in str(Num):
        Digits.append(digit)

    DigitsRev = Digits[:]
    DigitsRev.reverse()
    return Digits == DigitsRev

#Main
Factor1 = 999
Factor2 = 999
NumLst = []

while Factor1 >= 900:
    Factor2 = 999
    while Factor2 >= 900:
        NumLst.append(Factor1*Factor2)
        Factor2 -= 1
    Factor1 -= 1

NumLst.sort(reverse=True)
for i in NumLst:
    if IsPalindromicNumber(i):
        print i
        break
