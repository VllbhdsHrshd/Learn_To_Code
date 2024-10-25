## Canadian Calorie Problem

'''

Here are the three burger choices:
1 – Cheeseburger (461 Calories)
2 – Fish Burger (431 Calories)
3 – Veggie Burger (420 Calories)
4 – no burger

Here are the three side order choices:
1 – Fries (100 Calories)
2 – Baked Potato (57 Calories)
3 – Chef Salad (70 Calories)
4 – no side order


Here are the three drink choices:
1 – Soft Drink (130 Calories)
2 – Orange Juice (160 Calories)
3 – Milk (118 Calories)
4 – no drink


Here are the three dessert choices:
1 – Apple Pie (167 Calories)
2 – Sundae (266 Calories)
3 – Fruit Cup (75 Calories)
4 – no dessert

'''

burger_cal = {1:461,2:431,3:420,4:0}
sideorder_cal = {1:100, 2:57, 3:70, 4:0}
drink_cal = {1:130,2:160,3:118,4:0}
dessert_cal = {1:167, 2:266, 3:75, 4:0}

l = int(input())
m = int(input())
n = int(input())
o = int(input())


total_cal = burger_cal[l] + sideorder_cal[m] + drink_cal[n] + dessert_cal[o]

print(f'Your total Calorie count is {total_cal}.')
