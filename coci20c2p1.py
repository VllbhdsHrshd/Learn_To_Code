n = int(input())
inp = input()

i,j = 0,0
record = {'+':0, '*':0, '-':0, '=':0}
while i < n - 1:
    if inp[i]==inp[i+1]:
        i+=1
    else:
        length = -(j - i)+1
        if record[inp[i]]<length:
            record[inp[i]] = length
        j = i + 1
        i = j


if inp[i]==inp[i-1]and j<i:
    length = i - j +1
    if record[inp[i]]<length:
        record[inp[i]] = length
elif i==j:
    if record[inp[i]]<1:
        record[inp[i]] = 1
        
#print(record)
mm = -1
for k,v in record.items():
    mm = max(v, mm)

output_matrix = [['.' for _ in range(n)] for _ in range(mm)]
print(output_matrix)


    
        
    

