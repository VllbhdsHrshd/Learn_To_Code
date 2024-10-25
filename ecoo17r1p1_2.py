# School Trips...........
year_cost = [12, 10, 7 ,5]

for dataset in range(10):

    trip_cost = int(input())
    proportions = input().split()
    num_studs = int(input())


    for i in range(len(proportions)):
        proportions[i] = float(proportions[i])

    studs_per_year = []

    for i in range(len(proportions)):
        studs_per_year.append(int(proportions[i] * num_studs))


    counted = sum(studs_per_year)
    uncounted = num_studs - counted
    most = max(studs_per_year)
    where = studs_per_year.index(most)
    studs_per_year[where] += uncounted


    total_raised = 0

    for i in range(len(studs_per_year)):
        total_raised += studs_per_year[i] * year_cost[i]

    if total_raised/2 < trip_cost:
        print('YES')
    else:
        print('NO')



