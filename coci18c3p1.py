## Honi Block.......

word = input()


count_honi = 0

#f = 'PROHODNIHODNIK'

#word = f

#print(word, len(word))


target = ['H','O','N','I']
i,j = 0,0
for i in range(len(word)):
    if word[i] == target[j]:
        
        #print(i, j)    
        
        if word[i] == 'I' and j == 3:
            count_honi += 1
            j = 0
        else:
            j += 1

print(count_honi)


