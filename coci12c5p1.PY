## Rijeci...

K = int(input())

count_a , count_b = 1, 0
# Rules -
## A -> B
## B -> BA

for _ in range(K):
    #print(count_a, count_b)
    count_a, count_b = count_b, count_a + count_b
    
print(count_a, count_b)

