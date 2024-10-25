## Apple Vs Banana...
app_3 = int(input())
app_2 = int(input())
app_1 = int(input())

ban_3 = int(input())
ban_2 = int(input())
ban_1 = int(input())

app_score = app_3 * 3 + app_2 * 2 + app_1 
ban_score = ban_3 * 3 + ban_2 * 2 + ban_1

if app_score>ban_score:
    print('A')
elif ban_score>app_score:
    print('B')
else:
    print('T')
    

