# ccc00s2
## Babbling Brooks
n = int(input())

streams, splitJoin = [], []
for _ in range(n):
    streams.append(int(input()))

done = False

while not done:
    i = int(input())
    if i==77:
        done = True

    elif i==99:
        splitJoin.append(i)
        splitJoin.append(int(input()))
        splitJoin.append(int(input()))

    elif i==88:
        splitJoin.append(i)
        splitJoin.append(int(input()))


## [99 1 50 88 3 88 2 77]
i,j=0,0
temp = []
while i<len(spplitJoin):
    if splitJoin[i]==99:
        streamTobeSplit = splitJoin[i+1] - 1
        proportion = splitJoin[i+2]
        left, center, right = streams[:streamTobeSplit], streams[streamTobeSplit], streams[streamTobeSplit+1:]
        leftFork, rightFork = center[0]*proportion, center[0]*(1-proportion)
        temp.append(leftFork)
        temp.append(rightFork)
        center = temp
        streams = left+center+right
        i+=3

    elif splitJoin[i]==88:
        mergePoint = splitJoin[i+1] - 1
        leftStream = streams[:mergePoint]

