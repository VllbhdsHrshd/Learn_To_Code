## English or French....


N = int(input())

s = ''

for i in range(N):
    temp = input()
    s += temp

#print(s)
count_s , count_t = 0,0
count_s += s.count('s')
count_s += s.count('S')
count_t += s.count('t')
count_t += s.count('T')

#print(count_s, count_t)

if count_s>=count_t:
    print('French')
else:
    print('English')
    





