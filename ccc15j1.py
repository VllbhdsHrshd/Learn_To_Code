month = int(input())
date = int(input())

check_date = 18
check_month = 2


if month<check_month:
    print('Before')
elif month>check_month:
    print('After')
else:
    if date<check_date:
        print('Before')
    elif date>check_date:
        print('After')
    else:
        print('Special')
        

