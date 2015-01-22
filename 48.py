n = 1
LastTenDigits = 0

while n <= 1000:
    No = str(n**n)
    if len(No) > 10:
        LastTenDigits += int(No[-10:])
    else:
        LastTenDigits += int(No)
    n += 1

print str(LastTenDigits)[-10:]
