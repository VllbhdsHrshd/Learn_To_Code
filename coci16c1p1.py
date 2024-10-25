# Data Plan

perMonth = int(input())
numMonths = int(input())
history = list(range(numMonths))

for i in range(numMonths):
    history[i] = int(input())

inStock = 0

#print(history, inStock)
for j in range(numMonths):
    inStock += perMonth - history[j]

print(inStock+perMonth)

    
    
    

