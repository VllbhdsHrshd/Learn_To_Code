# ccc00s2
## Babbling Brooks
n = int(input())

streams, splitJoin = [], []
for _ in range(n):
    streams.append(int(input()))

done = False
## [99 1 50 88 3 88 2 77]
while not done:
    i = int(input())
    if i==77:
        done = True

    elif i==99:
        splitIdx = int(input()) - 1
        temp = streams.pop(splitIdx)
        ratioSplit = int(input())
        leftFork, rightFork = round(temp*ratioSplit*0.01), round(temp*(1-ratioSplit*0.01))
        streams.insert(splitIdx,rightFork)
        streams.insert(splitIdx,leftFork)
        #print('After splitting:: ', streams, end=' ')

    elif i==88:
        joinIdx = int(input()) - 1
        leftStream = streams.pop(joinIdx)
        rightStream = streams.pop(joinIdx)
        finalFlow = leftStream+rightStream
        streams.insert(joinIdx, finalFlow)
        #print('After Merging', streams, end =' ')


for i in streams:
    print(i, end=' ')


