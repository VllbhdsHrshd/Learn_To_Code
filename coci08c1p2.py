## Ptice......

N = int(input())

## Adrian's take :: ABCABCABCABC...
## Bruno's Take :: BABCBABCBABC....
## Goran's Take :: CCAABBCCAABB....


correct_answer = input()

Adrian_ans = ['A','B','C']
Bruno_ans = ['B','A','B','C']
Goran_ans = ['C','C','A','A','B', 'B']
div_adrian = len(Adrian_ans)
div_bruno = len(Bruno_ans)
div_goran = len(Goran_ans)

sequens = [None] * N
ans_adr, ans_bru, ans_gor = [],[],[]

for i in range(N):
    ans_adr.append(Adrian_ans[i%div_adrian])
    ans_bru.append(Bruno_ans[i%div_bruno])
    ans_gor.append(Goran_ans[i%div_goran])

# score_Adrian, score_Bruno, score_Goran = 0,0,0
score = {'Adrian':0, 'Bruno':0,'Goran':0}

for i in range(N):
    # for adrian
    if correct_answer[i]==ans_adr[i]:
        score['Adrian']+=1

    if correct_answer[i]==ans_bru[i]:
        score['Bruno']+=1

    if correct_answer[i]==ans_gor[i]:
        score['Goran']+=1



sorted_score={k:v for k,v in sorted(score.items(), key= lambda x: x[1], reverse = True)}
winner = max(sorted_score, key = sorted_score.get)
#print(sorted_score)
print(sorted_score[winner])
# print(winner)
for k,v in sorted_score.items():
    if sorted_score[winner]==v:
        print(k)






