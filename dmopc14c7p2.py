# dmopc14c7p2
# Tides...
N = int(input())
tides_specs = list(map(int, input().split()))
'''
print(N)
print(tides_specs)
'''

min_idx = tides_specs.index(min(tides_specs))
max_idx = tides_specs.index(max(tides_specs))

# Bad Logic....Begins
#print(min_idx, max_idx)
if min_idx>max_idx:
    print('unknown')
else:
    check = False
    for i in range(min_idx, max_idx):
        if tides_specs[i] < tides_specs[i+1]:
            check = True
        else:
            check = False
            break
    if check:
        print(max(tides_specs)-min(tides_specs))
    else:
        print('unknown')
