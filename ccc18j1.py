## Telemarketers
x1 = input()
x2 = input()
x3 = input()
x4 = input()

condition_1, condition_2, condition_3 = False, False, False

first_fourth_digit = ['8','9']

if x1 in first_fourth_digit:
    condition_1 = True
else:
    pass

if x4 in first_fourth_digit:
    condition_2 = True
else:
    pass

if x2 == x3:
    condition_3 = True
else:
    pass


if condition_1 and condition_2 and condition_3:
    print('ignore')
else:
    print('answer')


