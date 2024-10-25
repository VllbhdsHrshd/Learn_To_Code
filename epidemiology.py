# Write your code here :-)
threshold = int(input())
today = int(input())
rate = int(input())

day = 0
prev_day = today

while today<=threshold:
    today += prev_day * rate
    prev_day *= rate
    day += 1

print(day)

