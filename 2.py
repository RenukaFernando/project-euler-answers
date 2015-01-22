FibonacciSequence1 = 1
FibonacciSequence2 = 2

NextValue = 3
TotalEvenValuedTerms = 2

while NextValue <= 4000000:
    if NextValue%2 == 0:
        TotalEvenValuedTerms += NextValue

    FibonacciSequence1 = FibonacciSequence2
    FibonacciSequence2 = NextValue
    NextValue = FibonacciSequence1 + FibonacciSequence2

print TotalEvenValuedTerms
