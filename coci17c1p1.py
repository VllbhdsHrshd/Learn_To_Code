# coci17c1p1
# Cezar

numCards = int(input())
numCards_drawn = []
for _ in range(numCards):
    numCards_drawn.append(int(input()))


cardCollection = {1:4, 2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:16,11:4}
difference = 21 - sum(numCards_drawn)

## updating the card collections

for i in range(numCards):
    cardCollection[numCards_drawn[i]]-=1

greaterThanDiff, lessThanDiff = 0,0

for k,v in cardCollection.items():
    if k > difference:
        greaterThanDiff+=v
    else:
        lessThanDiff += v

if greaterThanDiff>=lessThanDiff:
    print('DOSTA')
else:
    print('VUCI')


