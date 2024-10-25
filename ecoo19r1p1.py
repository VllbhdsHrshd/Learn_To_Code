# ecoo19r1p1
# Free Shirts......


for _ in range(10):

    dataset = input().split()
    N,M,D = int(dataset[0]), int(dataset[1]), int(dataset[2])

    events = {}
    M_inp = input().split()
    for i in M_inp:
        i = int(i) - 1
        if i in events:
            events[i]+=1
        else:
            events[i] = 1

    #print(events)


    #events = sorted(events)
    laundry_count = [0]*D
    cleaned_shirt, dirty_shirt = N,0

    for i in range(D):


        if cleaned_shirt==0:
            laundry_count[i] = 1
            cleaned_shirt=total
            dirty_shirt = 0


        if cleaned_shirt>0:
            cleaned_shirt-=1
            dirty_shirt+=1

        if i in events:
            cleaned_shirt+=events[i]


        ## Work
        #print('Clean: ', cleaned_shirt, ' ', 'Dirty Shirt ', dirty_shirt)
        total = cleaned_shirt+dirty_shirt
        #print('Total Shirts: ', total)



    #print(laundry_count)
    print(sum(laundry_count))










