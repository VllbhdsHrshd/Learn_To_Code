# Village Neighbourhood...

'''
## mY INCORRECT aPPROACH...
n = int(input())
villages = [-1] * n

for i in range(n):
    villages[i] = int(input())

# [-1, -1, -1, -1, -1]
neighbourhood = [0] * (n-1)
villages = sorted(villages)
for i in range(n-1):
    temp = villages[i+1] - villages[i]
    if temp>0:
        neighbourhood[i] = temp/2
    else:
        neighbourhood[i] = -temp/2

# print(neighbourhood)
print(f'{round(min(neighbourhood),1)}')
'''
## Correct Approach

n = int(input())
villages = []
for i in range(n):
    villages.append(int(input()))

villages = sorted(villages)

neighbourhood = []

for i in range(1, n-1):
    right = (villages[i+1] - villages[i])/2
    left =  (villages[i] - villages[i-1])/2
    neighbourhood.append(right + left)

print(f'{round(min(neighbourhood), 1)}')














