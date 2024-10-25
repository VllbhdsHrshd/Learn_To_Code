# ecoo18r1p2
## Rue's Rings

for _ in range(10):

    ## Do Stuffs here
    N = int(input())
    overall = [[] for _ in range(N)]
    for i in range(N):
        temp = list(map(int, input().split()))
        overall[i] = temp


    min_diameter = 700001
    res = [] ## format (id, min_element)
    for j in range(len(overall)):
        mini_element = min(overall[j][2:])
        res.append((overall[j][0], mini_element))
        min_diameter = min(mini_element, min_diameter)

    output_seq = list(map(lambda x:x[0],filter(lambda t:t[1]==min_diameter, res)))
    output_seq.sort()

    formatted_op ='{' + ','.join(map(str, output_seq)) + '}'


    print(str(min_diameter),formatted_op)













