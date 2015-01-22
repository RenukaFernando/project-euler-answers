Coins = [1,2,5,10,20,50,100,200]

MaxCoin = []
for i in Coins:
    MaxCoin.append(200/i)

DifferentWays = 0
for a in range(MaxCoin[0] + 1):
    print 'Wait...(' + str(a) + '/200)'
    for b in range(MaxCoin[1] + 1):
        if Coins[0]*a + Coins[1]*b > 200:
            break
        for c in range(MaxCoin[2] + 1):
            if Coins[0]*a + Coins[1]*b + Coins[2]*c > 200:
                break
            for d in range(MaxCoin[3]+ 1):
                if Coins[0]*a + Coins[1]*b + Coins[2]*c + Coins[3]*d > 200:
                    break
                for e in range(MaxCoin[4] + 1):
                    if Coins[0]*a + Coins[1]*b + Coins[2]*c + Coins[3]*d + Coins[4]*e > 200:
                        break
                    for f in range(MaxCoin[5] + 1):
                        if Coins[0]*a + Coins[1]*b + Coins[2]*c + Coins[3]*d + Coins[4]*e + Coins[5]*f > 200:
                            break
                        for g in range(MaxCoin[6] + 1):
                            if Coins[0]*a + Coins[1]*b + Coins[2]*c + Coins[3]*d + Coins[4]*e + Coins[5]*f + Coins[6]*g > 200:
                                break
                            for h in range(MaxCoin[7] + 1):
                                if (Coins[0]*a + Coins[1]*b + Coins[2]*c + Coins[3]*d + Coins[4]*e + Coins[5]*f + Coins[6]*g + Coins[7]*h) > 200:
                                    break
                                if (200 == Coins[0]*a + Coins[1]*b + Coins[2]*c + Coins[3]*d + Coins[4]*e + Coins[5]*f + Coins[6]*g + Coins[7]*h):
                                    DifferentWays += 1

print DifferentWays
