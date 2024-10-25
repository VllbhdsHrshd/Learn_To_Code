# ecoo18r1p1
# Willow's Wild Ride

for _ in range(10):
    T,N = input().split()
    T, N = int(T),int(N)
    actions = []
    for _ in range(N):
        temp = input()
        if temp=='B':
            actions.append(1)
        else:
            actions.append(0)



    ## Processing...
    ## [01010]
    #print('The Sequence is:: ', actions)
    counter = 0
    for i in range(len(actions)):


        if actions[i]==0:
            pass
        else:
            counter+=T
        #print('counter value:: ', counter)
        if counter>0:
            counter -= 1

    print(counter)













