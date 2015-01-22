F = open("59(Enscryption).txt")
Enscr = F.readline().split(",")
F.close()

LowerLetters = range(97, 123) #Here 97 = 'a',122 = 'z'
As, Bs, Cs = [], [], [] #Password = ABC
#common letter in 32 - 122

Count = len(Enscr)
Break = False

def Decrypt(Place, Lst):
    key = 97
    while key <= 122:
        for letter in range(Place, Count, 3):
            if 32 <= int(Enscr[letter]) ^ key <= 122:
                'common letter'
            else:
                break
        else:
            Lst.append(key)
            
        key += 1

Decrypt(0, As)
Decrypt(1, Bs)
Decrypt(2, Cs)

print 'Select the text that contains common English words\n'
Step = 1
SampleCount = 100
Keys = []
for key0 in As:
    for key1 in Bs:
        for key2 in Cs:
            Sample = ''
            for letter in range(SampleCount):
                WhatKey = letter % 3
                if WhatKey == 0: Sample += chr(int(Enscr[letter]) ^ key0)
                if WhatKey == 1: Sample += chr(int(Enscr[letter]) ^ key1)
                if WhatKey == 2: Sample += chr(int(Enscr[letter]) ^ key2)
            print str(Step) + ').\t' + Sample + '\n'
            Keys.append([key0, key1, key2])
            Step += 1

StepsCount = len(As) * len(Bs) * len(Cs)
while True:
    try:
        TheKey = int(raw_input("Enter the appropriate number (Between 1 - " + str(StepsCount) + ') :'))
        if 1 <= TheKey <= StepsCount:
            break
        else:
            print 'Please Enter a number Between 1 - ' + str(StepsCount) + '.....'
    except:
        print 'Please Enter a number.....'

Sum = 0
for letter in range(len(Enscr)):
    WhatKey = letter % 3
    if WhatKey == 0: Sum += int(Enscr[letter]) ^ Keys[TheKey-1][0]
    if WhatKey == 1: Sum += int(Enscr[letter]) ^ Keys[TheKey-1][1]
    if WhatKey == 2: Sum += int(Enscr[letter]) ^ Keys[TheKey-1][2]

print Sum
