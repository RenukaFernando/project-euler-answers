f = open("13.txt")
Sum = 0

for i in range(100):
    Sum += int(f.readline())

f.close()
print str(Sum)[0:10]
