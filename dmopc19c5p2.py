
## This Solution didn't work as expected from it to be....
MH = list(map(int, input().split()))
Moves, Health = MH[0], MH[1] 

Action_Charlie = []
Action_Opponent = []

for _ in range(Moves):
    temp = input().split()
    action = temp[0]
    damage = int(temp[1])
    Action_Charlie.append((action, damage))
    

for _ in range(Moves):
    temp = input().split()
    action = temp[0]
    damage = int(temp[1])
    Action_Opponent.append((action, damage))

Charlie_Health, Opp_Health = Health, Health 
Charlie_lost, Opp_Lost = False, False
for i in range(Moves):
    C_action = Action_Charlie[i][0]
    C_damage = Action_Charlie[i][1]
    Opp_action = Action_Opponent[i][0]
    Opp_damage = Action_Opponent[i][1]
    
    
    if C_action=='A' and Opp_action=='A':
        Charlie_Health -= Opp_damage
        Opp_Health -= C_damage
        
        if Charlie_Health<=0:
            Charlie_lost = True
            break
        if Opp_Health<=0:
            Opp_Lost = True
            break
    elif C_action=='D' and Opp_action=='D':
        # Charlie ki Thukai
        Charlie_Health -= C_damage
        if Charlie_Health<=0:
            Charlie_lost = True
            break
    elif C_action == 'A' and Opp_action =='D':
        Charlie_Health -= Opp_damage
        Opp_Health -= C_damage
        if Charlie_Health<=0:
            Charlie_lost = True
            break
        if Opp_Health<=0:
            Opp_Lost = True
            break
    
    else:
        Charlie_Health -= Opp_damage
        Opp_Health -= C_damage
        if Charlie_Health<=0:
            Charlie_lost = True
            break
        if Opp_Health<=0:
            Opp_Lost = True
            break

    
    
    


if Charlie_lost and not Opp_Lost:
    print("DEFEAT")
elif Opp_Lost and not Charlie_lost:
    print("Victory")
else:
    print('TIE')
    
    
    

    
    
    
