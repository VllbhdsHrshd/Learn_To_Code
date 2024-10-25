# A long time ago in a galaxy far away...

precedent = 'A long time ago in a galaxy '
middle = 'far, '
antecedent = 'far away...'

N = int(input())

if N==1:
    print(precedent+antecedent)
else:
    middle *= (N-1)
    print(precedent+middle+antecedent)

