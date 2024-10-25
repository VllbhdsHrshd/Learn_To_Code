# School Trip
total_money = int(input())
proportion = input()
total_studs = int(input())
'''
print(total_money, type(total_money),proportion,
type(proportion),total_studs, type(total_studs))
'''
proportion = proportion.split()

for i in range(len(proportion)):
    proportion[i] = float(proportion[i])

copyProportion = proportion[:]

price_contributions = [12,10,7,5]
total_proportion = sum(proportion)

for i in range(len(proportion)):
    proportion[i] = total_studs * proportion[i]

if sum(proportion)==float(total_studs):
    extra = False
else:
    extra = True

if extra:
    for i in range(len(proportion)):
        proportion[i] = round(proportion[i])
    excess = -sum(proportion) + total_studs
    if excess<0:
        excess = -excess

    max_idx = proportion.index(max(proportion))
    proportion[max_idx] += excess
    money = []
    for i in range(len(proportion)):
        moneya.ppend(proportion[i] * price_contributions[i])

    if sum(money)>=total_money:
        print('YES')
    else:
        print('NO')


else:

    money = []

    for i in range(len(proportion)):
        money.append(proportion[i] *  price_contributions[i])

    if sum(money)>=total_money:
        print('YES')
    else:
        print('NO')














