
## CC and CheeseKun....

width = int(input())
percentage=int(input())

status = ''

if width==3 and percentage>=95:
    status = 'absolutely'

elif width == 1 and percentage<=50:
    status = 'fairly'
else:
    status = 'very'
    
print(f'C.C. is {status} satisfied with her pizza.')
