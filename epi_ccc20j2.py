# Write your code here :-)
threshold = int(input())
initial = int(input())
rate = int(input())

total, day = initial, 0


while total <= threshold:
    day+=1
    initial *= rate
    total += initial

print(day)

