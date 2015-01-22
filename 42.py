f = open('42.txt')

Value = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def IsTriagnleWord(WordValue):
    N = round((WordValue * 2)**0.5,0)
    return 2*WordValue == N*(N+1)

Words = f.read().split('","')
f.close()
Words[0] = Words[0].replace('"', '')
Words[len(Words) - 1] = Words[len(Words) - 1].replace('"', '')

TrianglewordsCount = 0
for Word in Words:
    WordValue = 0
    for letter in Word:
        WordValue += (Value.index(letter) + 1)

    if IsTriagnleWord(WordValue):
        TrianglewordsCount += 1

print TrianglewordsCount


