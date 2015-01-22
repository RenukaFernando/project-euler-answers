f = open("54(Poker).txt")

Poker = []
for Hand in range(1000):
    Poker.append(f.readline().split())

f.close

def HandValues(Hand):
    'Return True if Same Suit'
    'Hand = [[Gruoped Values'
    '[4], [3], [2], [1]], IsSameSuit]'
    SameSuit = True
    Suit1 = Hand[0][1]
    
    'Return the Values of each cards in a hand'
    Values = []
    for Card in Hand:
        'Find the Value'
        try:
            Value = int(Card[0])
        except:
            Value = Card[0]
            if Value == 'T': Value = 10
            if Value == 'J': Value = 11
            if Value == 'Q': Value = 12
            if Value == 'K': Value = 13
            if Value == 'A': Value = 14

        Values.append(Value)

        'Return True if Same Suit'
        if Card[1] != Suit1:
            SameSuit = False

    Values.sort(reverse = True)

    return [GroupValues(Values), SameSuit]

def GroupValues(Values):
    'Group Values if same values'
    G4, G3, G2, G1 = [], [], [], []
    Count = 1
    for CardNo in range(4):
        Card = Values[CardNo]
        CardNext = Values[CardNo + 1]
        if Card == CardNext:
            Count += 1
        else:
            if Count == 1: G1.append(Card)
            if Count == 2: G2.append(Card)
            if Count == 3: G3.append(Card)
            if Count == 4: G4.append(Card)
            Count = 1

    if Count == 1: G1.append(CardNext)
    if Count == 2: G2.append(CardNext)
    if Count == 3: G3.append(CardNext)
    if Count == 4: G4.append(CardNext)

    return [G4, G3, G2, G1]

def IsConsecutive(Values):
    'Return True if Consecutive'
    for CardNo in range(1, 5):
        if Values[CardNo] != Values[0] - CardNo:
            return False
    return True

def Rank(Hand):
    'Check, what is the rank of a hand'
    Hand = HandValues(Hand)
    'Hand = [[Gruoped Values [4], [3], [2], [1]], IsSameSuit]'
    SameSuit = Hand[1]
    AllDifferent = len(Hand[0][3]) == 5
    
    'Royal Flush' #[Rank]
    if SameSuit and Hand[0][3] == [14, 13, 12, 11, 10]:
        return [10]

    'Straight Flush' #[Rank, Highest]
    if SameSuit and IsConsecutive(Hand[0][3]):
        return [9, Hand[0][3][0]]

    'Four of a Kind' #[Rank, Highest of Same 4, Remain]
    if len(Hand[0][0]) == 1:
        return [8, Hand[0][0][0], Hand[0][3][0]]

    'Full House' #[Rank, Highest of Same 3, Highest of Same 2]
    if len(Hand[0][1]) == 1 and len(Hand[0][2]) == 1:
        return [7, Hand[0][1][0], Hand[0][2][0]]

    'Flush' #[Rank, CardList]
    if SameSuit:
        return [6, Hand[0][3]]

    'Straight' #[Rank, Highest]
    if AllDifferent and IsConsecutive(Hand[0][3]):
        return [5, Hand[0][3][0]]

    'Three of a Kind' #[Rank, Highest of Same 3, RemainList]
    if len(Hand[0][1]) == 1:
        return [4, Hand[0][1][0], Hand[0][3]]

    'Two Pairs' #[Rank, List of Same 2, Remain]
    if len(Hand[0][2]) == 2:
        return [3, Hand[0][2], Hand[0][3][0]]

    'One Pair' #[Rank, Highest of Same, RemainList]
    if len(Hand[0][2]) == 1:
        return [2, Hand[0][2][0], Hand[0][3]]

    'High Card' #[Rank, RemainList]
    return [1, Hand[0][3]]

'Find How many hands does Player 1 win?....................................'
Count = 0 #Player 1 won;
for Hand in range(1000):
    Player1 = Rank(Poker[Hand][:5])
    Player2 = Rank(Poker[Hand][5:])

    if Player1 > Player2:
        Count += 1

print Count

