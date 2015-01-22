Num1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
Num2 = ['ten', 'eleven', 'twelve', 'thirteen','fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
Num3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

Num1Count = 0
for i in Num1:
    Num1Count += len(i)

Num2Count = 0
for i in Num2:
    Num2Count += len(i)

Num3Count = 0
for i in Num3:
    Num3Count += len(i)

LetterCount1to99 = Num1Count + Num2Count + Num1Count * len(Num3) + Num3Count * len(Num1) + Num3Count
LetterCountHundred = Num1Count + len(Num1) * len('Hundred')
LetterCountHundred1to99 = (Num1Count + len(Num1) * len('HundredAnd')) * 99

print LetterCount1to99 * 10 + LetterCountHundred + LetterCountHundred1to99 + len('OneThousand')
