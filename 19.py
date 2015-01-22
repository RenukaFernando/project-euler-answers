def IsLeapYear(year):
    if year % 400 == 0:
        return 1
    elif year % 100 == 0:
        return 0
    elif year % 4 == 0:
        return 1

def DaysOfMonth(Month, year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif IsLeapYear(year):
        return 29
    else:
        return 28
        
year = 1900
month = 1
day = 1 #1 Means Monday (1 --> Monday)
SundayCount = 0

while year < 2001:
    while month < 13:
        day = (DaysOfMonth(month, year) + day)%7
        if day == 0 and year > 1900:
            SundayCount += 1
        month += 1
    year += 1
    month = 1

print SundayCount
