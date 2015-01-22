f = open("11.txt")
NumLst = []
for row in range(20):
    NumLst.append(f.readline().split())
f.close()

MaxVal = 1
#Check Right to Left
for row in NumLst:
    n = 0
    while n < 17:
        product = 1
        for i in range(4):
            product *= int(row[n + i])
        if product > MaxVal:
            MaxVal = product
        n += 1

#Check Up to Down
col = 0
while col < 20:
    row = 0
    while row < 17:
        product = 1
        for i in range(4):
            product *= int(NumLst[row + i][col])
        if product > MaxVal:
            MaxVal = product
        row += 1
    col += 1

#Check diagonal \
col = 0
while col < 17:
    row = 0
    while row < 17:
        product = 1
        for i in range(4):
            product *= int(NumLst[row + i][col + i])
        if product > MaxVal:
            MaxVal = product
        row += 1
    col += 1

#Check diagonal /
col = 19
while col > 3:
    row = 0
    while row < 17:
        product = 1
        for i in range(4):
            product *= int(NumLst[row + i][col - i])
        if product > MaxVal:
            MaxVal = product
        row += 1
    col -= 1

print MaxVal
