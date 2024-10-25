## Slot Machines
## Slot 1 machine pays 30 per every 35 play
## Slot 2 machine pays 60 per every 100 play
## Slot 3 machine pays 9 per every 10 play

#input 1
money = int(input())
#input 2 
counter_1 = int(input())
#input 3
counter_2 = int(input())
# input 4 
counter_3 = int(input())

## plays
playCounter = 0

#print('Money:: ',money,'counter_1:: ',counter_1,'counter_2:: ',counter_2,'counter_3:: ',counter_3)




while money>0:
    
    
    ## Machine 1
    money -= 1
    counter_1 += 1
    playCounter += 1
    if not money:
        break
    
    if counter_1 % 35 == 0:
        money += 30
    
    
    ## Machine 2
    money -= 1
    counter_2 +=1
    playCounter += 1
    if not money:
        break
    
    if counter_2 % 100 == 0:
        money += 60
    
    
    ## Machine 3
    money -= 1
    counter_3 += 1
    playCounter += 1
    if not money:
        break
    
    if counter_3 % 10 == 0:
        money += 9
    
    
    
    #print(money, counter_1, counter_2, counter_3, playCounter)


#print(money,counter_1 ,counter_2, counter_3,playCounter)
print('Martha plays',playCounter,'times before going broke.')

    





