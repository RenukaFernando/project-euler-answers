SumOfTheSquares = 0
SquareOfTheSum = 0

for i in range(1,101):
    SumOfTheSquares += i**2
    SquareOfTheSum += i

print SquareOfTheSum ** 2 - SumOfTheSquares
