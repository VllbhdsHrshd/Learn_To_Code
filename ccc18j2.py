## Occupied Spaces...

num_parkingSpace = int(input())
day_1 = input()
day_2 = input()

occ_parkingSpace = 0

for i in range(num_parkingSpace):
    if day_1[i]=='C' and day_2[i]=='C':
        occ_parkingSpace+=1


print(occ_parkingSpace)


    