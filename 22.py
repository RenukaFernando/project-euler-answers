f = open('22.txt')

TotalScore = 0
Mark = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Position = 1

Names = f.read().split('","')
f.close()
Names[0] = Names[0].replace('"', '')
Names[len(Names) - 1] = Names[len(Names) - 1].replace('"', '')
Names.sort()

for Name in Names:
    Score = 0
    for letter in Name:
        Score += (Mark.index(letter) + 1)
    Score *= Position
    if Position == 937:
        print Score
    TotalScore += Score
    Position += 1

print TotalScore

