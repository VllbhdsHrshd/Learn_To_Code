# Deal or No Deal....
## ccc07j3

deno = {1:10, 2:500, 3:1000, 4:5000,5:10000, 6:25000,
7:50000, 8:100000, 9:500000, 10:1000000}


num_opened = int(input())
opened = []
for _ in range(num_opened):
    opened.append(int(input()))

amount = int(input())

new_deno = []

for k,v in deno.items():
    if k not in opened:
        new_deno.append(v)

if (sum(new_deno)/(len(new_deno))) < amount:
    print('deal')
else:
    print('no deal')




