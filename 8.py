N1000file = open("8.txt")
N1000 = N1000file.read()
N1000file.close()

N1000 = N1000.replace('\n','') #removing line spaces

MaxProduct = 0
for i in range(0,1000-13):
    Product = 1
    for Num in N1000[i:i+13]:
        Product *= int(Num)
    if MaxProduct < Product:
        MaxProduct = Product

print MaxProduct
