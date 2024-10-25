## Multiple Choice..............


numQues = int(input())
QA = []
for i in range(2*numQues):
    temp = input()
    QA.append(temp)

#print(QA)
ques = QA[:numQues]
ans = QA[numQues:]
count = 0
for i,j in zip(ques, ans):
    if i == j:
        count+=1
print(count)

