# coci18c2p1
## PreoKret...

timed_A_Score = []
timed_B_Score = []

A = int(input())
for _ in range(A):
    timed_A_Score.append(int(input()))

B = int(input())
for _ in range(B):
    timed_B_Score.append(int(input()))


total_timed_Score = sorted(timed_A_Score + timed_B_Score)

victor = 'A' if total_timed_Score[0] in timed_A_Score else 'B'
score_array = []
half_time = 1440
score_before_halfTime = 0
for i in total_timed_Score:
    if i <= half_time:
        score_before_halfTime+=1
    else:
        break





score_A, score_B = int('A'==victor),int('B'==victor)
score_array.append(victor)
for i in range(1,len(total_timed_Score)):
    if total_timed_Score[i] in timed_A_Score:
        score_array.append('A')
    else:
        score_array.append('B')


A_count, B_count = 0,0

for i in range(1, len(score_array)):
    if score_array[i]=='A':
        score_A+=1
    else:
        score_B += 1

    if score_A>score_B and victor!='A':
        A_count+=1
        victor = 'A'
    if score_B>score_A and victor!='B':
        B_count+=1
        victor='B'

print(score_before_halfTime)
print(A_count+B_count)









