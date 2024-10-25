
Malik = input()

numBattle = int(input())

Ghulam = None
battleCount = 0

for _ in range(numBattle):
    temp_M, temp_G = input().split()
    #print(temp_M, temp_G)
    if temp_G == Malik:
        Malik = temp_M
    if Malik == temp_G or Malik == temp_M:
        battleCount+=1


print(Malik)
print(battleCount)
'''

X
4
A X
B X
X A
D A
'''
    
# Alternate Solution
#obeys = input()
#n = int(input())

#obeyed = obeys  # Contains one copy of each wizard that the wand obeyed

#for i in range(n):
    #line = input()
    #winner = line[0]
    #loser = line[2]
    #if obeys == loser:
        #obeys = winner
        #if not winner in obeyed:
            #obeyed = obeyed + winner

#print(obeys)
#print(len(obeyed))