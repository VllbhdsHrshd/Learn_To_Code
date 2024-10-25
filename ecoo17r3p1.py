# Baker Bonus
# ecoo17r3p1

for dataset in range(10):
    lst = input().split()
    franchisees = int(lst[0])
    days = int(lst[1])

    grid = []
    for i in range(days):
        row = input().split()
        for j in range(franchisees):
            row[j] =  int(row[j])

        grid.append(row)

    bonuses = 0

    for row in grid:
        total = sum(row)
        if total%13==0:
            bonuses+=total//13

    for col_idx in range(franchisees):
        total = 0
        for row_idx in range(days):
            total += grid[row_idx][col_idx]
        if total%13==0:
            bonuses+=total//13

    print(bonuses)


