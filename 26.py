n = 2
MaxCycle = 0

while n < 1000:
    RecurringCycle = []
    R = 1 % n
    while not(R in RecurringCycle) and R != 0:
        RecurringCycle.append(R)
        R = (R * 10) % n
    
    if R == 0:
        n += 1
        continue
    Cycle = len(RecurringCycle) - RecurringCycle.index(R)

    if Cycle > MaxCycle:
        MaxCycle = Cycle
        N = n

    n += 1

print N
