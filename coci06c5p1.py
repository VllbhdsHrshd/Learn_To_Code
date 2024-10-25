## Three Cups
#LMR
#LMR -> MLR 1st
#LMR -> LRM 2nd
#LMR -> RML 3rd

swaps = input()

ball_location = 1

for swap in swaps:
    if swap=='A' and ball_location==1:
        ball_location = 2
    elif swap == 'A' and ball_location == 2:
        ball_location = 1
    elif swap =='B' and ball_location == 2:
        ball_location = 3
    elif swap =='B' and ball_location == 3:
        ball_location = 2
    elif swap =='C' and ball_location == 1:
        ball_location = 3
    elif swap == 'C' and ball_location==3:
        ball_location =1
        
print(ball_location)

