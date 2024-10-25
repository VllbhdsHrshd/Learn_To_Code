# run length encoding
# My partially correct approach ....
'''
N = int(input())

while N>0:

    x = input()
    tempList = ''
    i,j = 1,0
    for i in range(1, len(x)):
        if i+1 != len(x) and x[i]==x[i+1]:
            pass
        else:
            tempList+=str(i-j+1)
            tempList+=' '
            tempList+=x[i]
            tempList+=' '
            #i+=1
            j = i + 1

    #if x[i] == x[i-1]:
     #   tempList+=str(i-j+1)
      #  tempList+=x[i]
    #else:
     #   tempList+=str(1)
      #  tempList+=x[i]

    print(tempList)




    N -= 1

'''
# Alternate approach
N = int(input())

for k in range(N):
    result = ''
    line =  input()
    total = 1

    for i in range(len(line) - 1):
        if line[i] == line[i+1]:
            total += 1
        else:
            result += f'{total} {line[i]}'
    result += f'{total}{line[-1]}'

    print(result)





