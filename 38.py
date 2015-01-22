Max = 9999 #99990000 + 2*9999 = 100009998
MaxPandigital = 0

for n in range(1, Max + 1):
    Val = n
    i = 1
    while Val < 10**10:
        Value = Val
        i += 1
        Val = Val * 10**len(str(n*i)) + n*i

    if len(str(Value)) != 9:
        continue

    if any(not(str(i) in str(Value)) for i in range(1, 10)):
        continue

    if MaxPandigital < Value:
        MaxPandigital = Value

print MaxPandigital

